# common/forms.py
from django import forms
from about.models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message")
