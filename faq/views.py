from django.shortcuts import render
from django.contrib import messages
from .models import Question
from common.forms import CollaborateForm


def faq_view(request):
    questions = Question.objects.all()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Message received! You can expect a response "
                "within 2 working days.",
            )
            # Redirect or re-render with success message can be added here

    collaborate_form = CollaborateForm()

    context = {
        'questions': questions,
        'form': collaborate_form
    }

    return render(request, "faq/faq.html", context)
