from django.shortcuts import render
from django.contrib import messages
from .models import Subscribe
from .forms import SubscribeForm


def subscribe_view(request):
    """
    Handle the display and submission of subscribe requests.

    This view allows users to send subscribe requests through a form.
    Upon successful subscription, a success message will be displayed.

    **Template**
    :template:`subscribe/subscribe.html`

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered subscribe page with the subscribe information
        and form.
    """

    if request.method == "POST":
        subscribe_form = SubscribeForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(
                request,
                "Subscription received! You can expect our next newsletter.",
            )

    subscribe = Subscribe.objects.all().order_by("-updated_on").first()
    subscribe_form = SubscribeForm()

    return render(
        request,
        "subscribe/subscribe.html",
        {"subscribe": subscribe, "subscribe_form": subscribe_form},
    )
