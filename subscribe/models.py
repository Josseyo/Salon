from django.db import models
from django.shortcuts import reverse


class Subscribe(models.Model):
    """Model representing a subscription.

    Attributes:
        title (CharField): The title of the subscription.
        updated_on (DateTimeField): The date and time when the
        subscription was last updated.
        content (TextField): The content of the subscription.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """Return the string representation of the subscription title."""
        return self.title


class SubscribeRequest(models.Model):
    """Model representing a subscription request.

    Attributes:
        email (EmailField): The email address of the subscriber,
        must be unique.
        date (DateTimeField): The date and time when the subscription
        request was created.
    """
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
        """Return the URL to redirect to after a successful subscription
        request.

        Returns:
            str: The URL to redirect to.
        """
        return reverse('home')
