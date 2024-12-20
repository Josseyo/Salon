from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import Http404

from .models import Product, Category
from .forms import ProductForm


def product_meeting_view(request, product_id, meeting_id):
    """Render the product meeting page if the meeting link is valid.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The ID of the product.
        meeting_id (str): The unique meeting ID.

    Raises:
        Http404: If the meeting link is invalid.

    Returns:
        HttpResponse: The rendered product meeting page.
    """
    product = get_object_or_404(Product, id=product_id)
    if meeting_id not in product.meeting_link:
        raise Http404("Invalid meeting link")
    return render(request, 'products/product_meeting.html', {'product': product})


def custom_404(request, exception):
    """Render the custom 404 error page.

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page.
    """
    return render(request, "404.html", status=404)


def all_products(request):
    """A view to show all products, including sorting and search queries.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered products page with filtered and sorted products.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if sortkey == "date":
                sortkey = "event_date"  # Changed from start_time to event_date
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The ID of the product.

    Returns:
        HttpResponse: The rendered product detail page.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered add product page or redirect to product detail.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(request, "Failed to add product. Please ensure the form is valid.")
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The ID of the product to edit.

    Returns:
        HttpResponse: The rendered edit product page or redirect to product detail.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(request, "Failed to update product. Please ensure the form is valid.")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store.

    Args:
        request (HttpRequest): The request object.
        product_id (int): The ID of the product to delete.

    Returns:
        HttpResponse: Redirect to the products page after deletion.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect(reverse("products"))
