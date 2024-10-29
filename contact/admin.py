from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """Admin panel for ContactFormAdmin"""

    list_display = (
        "name",
        "email",
        "read",
        "message",
    )
    list_filter = (
        "read",
        "name",
        "email",
    )
    search_fields = [
        "name",
        "email",
        "read",
        "message",
    ]
