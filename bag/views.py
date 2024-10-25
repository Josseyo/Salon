from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    print(f"Request method: {request.method}, item_id: {item_id}, POST data: {request.POST}")

    product = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity', 1)  # Default to 1 if not provided
    try:
        quantity = int(quantity)  # Convert to integer
    except ValueError:
        print(f"Invalid quantity input: {quantity}. Defaulting to 1.")
        quantity = 1

    redirect_url = request.POST.get('redirect_url', reverse('view_bag'))
    bag = request.session.get('bag', {})

    print(f"Current bag state before adding: {bag}")
    print(f"Adding quantity: {quantity} for item_id: {item_id}")

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    print(f"Updated bag state: {bag}")

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    print(f"Request method: {request.method}, item_id: {item_id}, POST data: {request.POST}")

    product = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity', 0)  # Default to 0 if not provided
    try:
        quantity = int(quantity)  # Convert to integer
    except ValueError:
        print(f"Invalid quantity input: {quantity}. Defaulting to 0.")
        quantity = 0

    bag = request.session.get('bag', {})
    print(f"Current bag state before adjustment: {bag}")

    if item_id in bag:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    print(f"Updated bag state after adjustment: {bag}")
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        
        print(f"Bag state before removal: {bag}")

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        print(f"Updated bag state after removal: {bag}")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        print(f"Error removing item: {e}")
        return HttpResponse(status=500)
