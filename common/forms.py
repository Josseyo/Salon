# common/forms.py
from django import forms
from contact.models import Contact
from django.core.validators import EmailValidator

class ContactForm(forms.ModelForm):
    responded = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message", "responded")

    email = forms.EmailField(validators=[EmailValidator()], error_messages={
        'invalid': 'Please enter a valid email address.'
    })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("This field is required.")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise forms.ValidationError("This field is required.")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("This field is required.")
        return message
