from django.db import models
from django.shortcuts import reverse


class Subscribe(models.Model):
    """Model representing a subscription."""
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """Return the string representation of the subscription title."""
        return self.title


class SubscribeRequest(models.Model):
    """Model representing a subscription request."""
    email = models.EmailField(
        unique=True,
        max_length=254,
        error_messages={'unique': "This email is already subscribed."}
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the string representation of the subscription request."""
        return f"Subscription request from {self.email}"

    def get_absolute_url(self):
        """Return the URL to redirect to after a successful
            subscription request."""
        return reverse('home')
