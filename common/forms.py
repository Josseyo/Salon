# common/forms.py
from django import forms
from contact.models import Contact
from django.core.validators import EmailValidator


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")

    email = forms.EmailField(validators=[EmailValidator()])
