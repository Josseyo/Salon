import uuid
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from django.core.exceptions import ValidationError


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model representing a product."""
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    event_date = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    host = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    meeting_link = models.URLField(max_length=255, null=True, blank=True)

    def clean(self):
        """Validate that start_time is before end_time."""
        if self.start_time >= self.end_time:
            raise ValidationError('End time must be after start time.')

    def __str__(self):
        """Return the string representation of the product."""
        return f"{self.name} on {self.event_date} from {self.start_time} to {self.end_time}"

    def generate_meeting_link(self):
        unique_id = uuid.uuid4().hex
        return reverse('product_meeting', args=[self.id, unique_id])

    def save(self, *args, **kwargs):
        if not self.meeting_link:
            self.meeting_link = self.generate_meeting_link()
        super().save(*args, **kwargs)
