from django.shortcuts import render, reverse
from .models import Contact
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from common.forms import ContactForm

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


class ContactFormCreateView(CreateView):
    """View to create a new contact form submission."""

    model = Contact
    form_class = ContactForm  # Use the ContactForm defined in common/forms.py

    def get_initial(self):
        """Set initial data for the form.

        Returns:
            dict: The initial data for the form, including the user's email if authenticated.
        """
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial["email"] = self.request.user.email
        return initial

    def get_success_url(self):
        """Return the URL to redirect after a successful form submission.

        Returns:
            str: The URL to redirect to after successful submission.
        """
        return reverse("contact-success")

    def form_valid(self, form):
        """Handle valid form submission.

        Args:
            form (ContactForm): The submitted contact form.

        Returns:
            HttpResponse: The response after successfully processing the form.
        """
        form.instance.author = self.request.user
        messages.info(self.request, "Message Sent!")
        return super().form_valid(form)


def contact_success(request):
    """Render the contact success page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered success page.
    """
    return render(request, "contact/contact_success.html")


class ContactListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """View to list all contact submissions."""

    model = Contact
    template_name = "contact/contact_list.html"
    context_object_name = "contacts"
    ordering = ["responded", "pk"]

    def test_func(self):
        """Check if the user is staff.

        Returns:
            bool: True if the user is staff, False otherwise.
        """
        return self.request.user.is_staff


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View to update a contact submission."""

    model = Contact
    fields = ["responded"]
    template_name_suffix = "_update_form"

    def _send_email(self):
        """Send the user a confirmation email.

        This method retrieves the email address and subject from the contact submission
        and sends an email using the provided body.

        Returns:
            None
        """
        email = self.object.email
        subject = self.object.subject
        body = self.request.POST.get("email_body", "No body provided.")
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

    def form_valid(self, form):
        """Handle valid form submission for updates.

        Args:
            form (ContactForm): The submitted contact form.

        Returns:
            HttpResponse: The response after successfully processing the form.
        """
        form.instance.author = self.request.user
        messages.info(self.request, "Response sent via email")
        self._send_email()
        form.instance.responded = True
        return super().form_valid(form)

    def test_func(self):
        """Check if the user is staff.

        Returns:
            bool: True if the user is staff, False otherwise.
        """
        return self.request.user.is_staff

    def get_success_url(self):
        """Return the URL to redirect after a successful update.

        Returns:
            str: The URL to redirect to after successful update.
        """
        return reverse("contact-update", kwargs={"pk": self.object.pk})


class ContactDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """View to delete a contact submission."""

    model = Contact
    success_url = reverse_lazy("contact-list")
    success_message = "Message Deleted."

    def test_func(self):
        """Check if the user is staff.

        Returns:
            bool: True if the user is staff, False otherwise.
        """
        return self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        """Handle the deletion of a contact submission.

        Args:
            request (HttpRequest): The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The response after deletion.
        """
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
