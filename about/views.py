from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_view(request):
    """
    Handle the display and submission of collaboration requests.

    This view allows users to send collaboration requests through a form.
    Upon successful submission, a success message will be displayed.

    **Template**
    :template:`about/about.html`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered about page with the contact information
        and form.
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Message received! You can expect a response "
                "within 2 working days.",
            )
    
    # Corrected 'about' to 'About'
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",  # Ensure the template path is correct
        {"about": about, "collaborate_form": collaborate_form},
    )
