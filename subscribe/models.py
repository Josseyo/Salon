from django.db import models
from django.shortcuts import reverse


class Subscribe(models.Model):

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class SubscribeRequest(models.Model):

    email = models.EmailField(
        unique=True,
        max_length=254,
        error_messages={'unique': "This email is already subscribed."}
        )

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Subscription request from {self.email}"

    def get_absolute_url(self):
        return reverse('home')
