from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Membership, UserMembership, Subscription

import stripe
stripe.api_key = "sk_test_OCu5QnGM8lYQBOG0BsQHtNHt00IKoPzlw6"



def get_user_membership(request):
    user_memnership_qs = UserMembership.objects.filter(user=request.user)
    
    if user_memnership_qs.exists():
        return user_memnership_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership=get_user_membership(request))
    
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(membership_type=membership_type)
    
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None
    


class MembershipSelectView(ListView):
    model = Membership
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        current_membership = get_user_membership(self.request)
        
        context['current_membership'] = str(current_membership.membership) 
        
        return context
    
    
    def post(self, request, **kwargs):
        selected_membership_type = request.POST.get('membership_type')
        
        user_membership     = get_user_membership(request)
        user_subscription   = get_user_subscription(request)
        
        selected_membership_qs = Membership.objects.filter(membership_type=selected_membership_type)
        
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()
            
        """
        VALIDATION
        """

        if user_membership.membership == selected_membership:
            if user_subscription != None:
                messages.info(request, 'you already own this membership')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        #assign to the session
        request.session['selected_membership_type'] = selected_membership.membership_type
        
        return HttpResponseRedirect(reverse('payment'))
    
@login_required    
def PaymentView(request):
     user_membership     = get_user_membership(request)
     selected_membership = get_selected_membership(request)
     
     publishKey = settings.STRIPE_PUBLISHABLE_KEY
     
     
     if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            cus = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            cus.source = token
            cus.save()
            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                     { "plan": selected_membership.stripe_plan_id },
                ]
            )
            return redirect(reverse('update_transactions', kwargs={
                'sub_id': subscription.id
            }))
        except stripe.error.CardError:
            messages.info(request, 'Your card has been declined')
             
     context = {
             'publishKey':publishKey,
             'selected_membership':selected_membership
         }
            
     return render(request, 'membership_payment.html', context)
 
 
def updateTransactions(request, subscription_id):
    user_membership            = get_user_membership(request)
    selected_membership        = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()
    
    sub, created               = Subscription.objects.get_or_create(user_membership=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.active                 = True
    sub.save()
    
    try:
        del request.session['selected_membership_type']
    except:
        pass
    
    messages.info(request, f'successfully created {selected_membership} memvership')
    return redirect(reverse('index'))
