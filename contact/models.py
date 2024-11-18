from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Contact(models.Model):
    """
    Model representing a contact request from a user.
    Attributes:
        name (str): The name of the person submitting the contact request.
        email (str): The email address of the person submitting the request.
        subject (str): The subject of the contact request, chosen from predefined options.
        message (str): The message content of the contact request.
        date_created (datetime): The date and time when the request was created.
        responded (bool): Indicates whether the request has been responded to.
    """

    class Meta:
        verbose_name_plural = "Contact Requests"

    SUBJECTS = (
        ("Trouble using the site", "Trouble using the site"),
        ("Ticket Issues", "Account Issues"),
        ("Event Issues", "Event Issues"),
        ("Other", "Other"),
    )

    name = models.CharField(
        max_length=254, default=""
    )
    email = models.EmailField(
        default="default@example.com"
    )
    subject = models.CharField(
        choices=SUBJECTS, max_length=254, default="Other"
    )
    message = models.TextField(
        max_length=1024, default=""
    )
    date_created = models.DateTimeField(default=timezone.now)
    responded = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of the contact request.

        Returns:
            str: The email address of the person who submitted the request.
        """
        return self.email
