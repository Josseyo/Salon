from django.shortcuts import render, reverse
from .models import Contact
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

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
    fields = ["email", "name", "subject", "message"]

    def get_initial(self):
        """Set initial data for the form."""
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial["email"] = self.request.user.email
        return initial

    def get_success_url(self):
        """Return the URL to redirect after a successful form submission."""
        return reverse("contact-success")

    def form_valid(self, form):
        """Handle valid form submission."""
        form.instance.author = self.request.user
        messages.info(self.request, "Message Sent!")
        return super().form_valid(form)


def ContactSuccess(request):
    """Render the contact success page."""
    return render(request, "contact/contact_success.html")


class ContactListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """View to list all contact submissions."""

    model = Contact
    template_name = "contact/contact_list.html"
    context_object_name = "contacts"
    ordering = ["responded", "pk"]

    def test_func(self):
        """Check if the user is staff."""
        return self.request.user.is_staff


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View to update a contact submission."""

    model = Contact
    fields = ["responded"]
    template_name_suffix = "_update_form"

    def _send_email(self):
        """Send the user a confirmation email."""
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
        """Handle valid form submission for updates."""
        form.instance.author = self.request.user
        messages.info(self.request, "Response sent via email")
        self._send_email()
        return super().form_valid(form)

    def test_func(self):
        """Check if the user is staff."""
        return self.request.user.is_staff

    def get_success_url(self):
        """Return the URL to redirect after a successful update."""
        return reverse("contact-update", kwargs={"pk": self.object.pk})


class ContactDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """View to delete a contact submission."""

    model = Contact
    success_url = reverse_lazy("contact-list")
    success_message = "Message Deleted."

    def test_func(self):
        """Check if the user is staff."""
        return self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        """Handle the deletion of a contact submission."""
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
