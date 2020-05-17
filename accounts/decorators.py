from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    """
    Decorator allows only unauthenticated users access registration and login pages.
    Authenticated users get redirected to home page.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    """Identify users that have permissions to access different parts of the website"""
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You don\'t have a permission to access this page')
                
        return wrapper_func
    return decorator


def admin_only(view_func):
    """Checks user group and redirects them to appropriate site"""
    def wrapper_func(request, *args, **kwargs):
        group = None
        
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
        if group == 'customer':
            return redirect('user-page')
        
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_func



# def members_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#        plan = None
       
#        if request.user.plans.exists():
#            plan = request.user.plans.all()[0].name
#            return redirect('progress')
#        else:
#            return HttpResponse('You don\'t have membership')
       
#     return wrapper_func


def members_only(view_func):
    def wrapper_func(self, request, pk, *args, **kwargs):
        plan_qs = Plan.objects.filter(pk=id)
        if plan_qs.exists():
            plan = plan_qs.first()
        
        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.user_membership_type
        
        pages_allowed_mem_types = plan.allowed_memberships.all()
        
        if pages_allowed_mem_types.filter(user_membership_type=user_membership_type).exists():
            return render(request, 'progress.html')
        
    return wrapper_func
           
 
       
        



