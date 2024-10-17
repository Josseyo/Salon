from django import forms
from .models import SubscribeRequest


class SubscribeForm(forms.ModelForm):
    class Meta:
        """
        Specify the Django model and order of the fields.
        """

        model = SubscribeRequest
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email",
                }
            ),
        }
        help_texts = {
            "email": "Submit your email and will send you our latest updates.",
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if SubscribeRequest.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email
