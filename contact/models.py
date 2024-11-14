from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Contact(models.Model):
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
        return self.email
