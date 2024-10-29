from django.shortcuts import render
from django.contrib import messages
from .models import Question
from common.forms import ContactForm


def faq_view(request):
    questions = Question.objects.all()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                "Message received! You can expect a response "
                "within 2 working days.",
            )
            # Redirect or re-render with success message can be added here

    contact_form = ContactForm()

    context = {
        'questions': questions,
        'form': contact_form
    }

    return render(request, "faq/faq.html", context)
