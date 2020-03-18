from django import forms
from .models import Order

class PaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range (2017, 2036)]
    
    credit_card_number = forms.CharField(label = 'Credit card number', required=False)
    cvv = forms.CharField(label= 'Security code', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name','last_name','phone_number','country', 'county', 'postcode', 'city', 'address1', 'address2')
    