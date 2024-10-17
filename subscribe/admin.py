from django.contrib import admin
from .models import SubscribeRequest

@admin.register(SubscribeRequest)
class SubscribeRequestAdmin(admin.ModelAdmin):
    """Admin panel for subscribeRequestAdmin"""

    list_display = (
        "email",
        "date",
    )
    list_filter = (
        "email",
        "date",
    )
    search_fields = [
        "email",
        "date",
    ]

