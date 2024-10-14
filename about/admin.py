from django.contrib import admin
from .models import CollaborateRequest


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """Admin panel for CollaborateRequestAdmin"""

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