from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'border-peach rounded-lg w-100'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'border-peach rounded-lg w-100'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Message...', 'class': 'border-peach rounded-lg message-textarea w-100'})
    )
