from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total >= settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE) / Decimal('100')
        discount_delta = 0
    else:
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total

    grand_total = total - discount

    # Debugging print statement
    print(f'Total: {total}, Discount: {discount}, Grand Total: {grand_total}')

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount_amount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
