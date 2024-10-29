# common/forms.py
from django import forms
from contact.models import ContactForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ("name", "email", "message")
