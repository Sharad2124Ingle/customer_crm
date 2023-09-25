from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import RetailUser
from .backends import RetailUserBackend

"""
class RetailUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = RetailUser
        fields = ['username', 'email', 'password', 'phone_no', 'shop_name', 'shop_id', 'mall_name', 'mall_id', 'address', 'city', 'state', 'zipcode']
"""

class RetailUserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = RetailUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_no']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.backend = RetailUserBackend.__module__ + "." + RetailUserBackend.__name__
        if commit:
            user.save()
        return user
