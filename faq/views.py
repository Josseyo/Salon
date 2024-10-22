from django.shortcuts import render
from .models import Question  # Import the Question model

def faq_view(request):
    questions = Question.objects.all()  # Fetch all questions

    # Prepare context data
    context = {
        'questions': questions  # Use the fetched questions here
    }

    return render(request, "faq/faq.html", context)  # Ensure the correct path to the template
