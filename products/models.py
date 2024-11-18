import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse


class Category(models.Model):
"""Model representing a product category."""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return the string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name

    def get_friendly_name(self):
        """Return the friendly name of the category.

        Returns:
            str: The friendly name of the category, if set.
        """
        return self.friendly_name


class Product(models.Model):
    """Model representing a product with event details."""

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
        """Validate that start_time is before end_time.

        Raises:
            ValidationError: If end_time is not after start_time.
        """
        if self.start_time >= self.end_time:
            raise ValidationError('End time must be after start time.')

    def __str__(self):
        """Return the string representation of the product.

        Returns:
            str: A formatted string representing the product, including name, event date, start time, and end time.
        """
        return f"{self.name} on {self.event_date} from {self.start_time} to {self.end_time}"

    def generate_meeting_link(self):
        """Generate a unique meeting link for the product.

        Returns:
            str: The URL for the product meeting.
        """
        unique_id = uuid.uuid4().hex
        return reverse('product_meeting', args=[self.id, unique_id])

    def save(self, *args, **kwargs):
        """Override the save method to set the meeting link if not already set.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        if not self.meeting_link:
            self.meeting_link = self.generate_meeting_link()
        super().save(*args, **kwargs)
