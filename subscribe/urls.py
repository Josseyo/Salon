from django.urls import path
from .views import subscribe_view

urlpatterns = [
    path("subscribe/", subscribe_view, name="subscribe"),
]
