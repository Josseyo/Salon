from django.db import models


# Create your models here.


class Contact(models.Model):
    """
    Model to store information about when and why to get in contact.

    Attributes:
        title (str): The title of the contact information.
        profile_image (CloudinaryField): An image associated with the contact.
        updated_on (datetime): The timestamp for when the contact information
        was last updated.
        content (str): Detailed content explaining the contact information.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """Return the title of the contact information."""
        return self.title


class ContactForm(models.Model):
    """
    Model to store contact details and request message.

    Attributes:
        name (str): The name of the person making the request.
        email (str): The email address of the person making the request.
        message (str): The message detailing the collaboration request.
        read (bool): A flag indicating whether the request has been read.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the collaboration request."""
        return f"Collaboration request from {self.name}"
