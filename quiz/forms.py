from django import forms
from .models import UserProfile, ContactMessage

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']