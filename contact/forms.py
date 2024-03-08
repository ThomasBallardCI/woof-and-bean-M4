from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name...', 'class': 'border-peach rounded-lg w-100'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email...', 'class': 'border-peach rounded-lg w-100'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Leave us a message...', 'class': 'border-peach rounded-lg message-textarea w-100'})
    )
