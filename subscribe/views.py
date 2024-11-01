from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscribe
from .forms import SubscribeForm


def subscribe_view(request):
    """Handle subscription requests and display the subscription form."""
    if request.method == "POST":
        subscribe_form = SubscribeForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(
                request,
                "Subscription received! You can expect our next newsletter.",
            )
            return redirect("subscribe")
    else:
        subscribe_form = SubscribeForm()

    subscribe = Subscribe.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "subscribe/subscribe.html",
        {"subscribe": subscribe, "subscribe_form": subscribe_form},
    )
