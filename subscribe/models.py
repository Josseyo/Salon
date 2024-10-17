from django.db import models


# Create your models here.


class Subscribe(models.Model):
    """
    Model to store information about why to signup for newsletter

    Attributes:
        title (str): The title of the contact information.
        updated_on (datetime): The timestamp for when the contact information
        was last updated.
        content (str): Detailed content explaining the subscription.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """Return the title of the contact information."""
        return self.title


class SubscribeRequest(models.Model):
    """
    Model to store email addresses
    Attributes:
        email (str): The email address of the person making the request.
        date (DateTime): The date indicating when the request was created.
    """

    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the collaboration request."""
        return f"Collaboration request from {self.email}"
