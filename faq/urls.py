# faq/urls.py
from django.urls import path
from .views import faq_view

urlpatterns = [
   path('', faq_view, name='faq'),  # Change here to have an empty string path
]

