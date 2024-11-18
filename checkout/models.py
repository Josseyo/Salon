import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Model representing a customer's order.

    Attributes:
        order_number: A unique identifier for the order.
        user_profile: The user profile associated with the order.
        full_name: The full name of the customer.
        email: The email address of the customer.
        phone_number: The phone number of the customer.
        country: The country where the order will be delivered.
        postcode: The postal code for the delivery address.
        town_or_city: The town or city for the delivery address.
        street_address1: The primary street address for delivery.
        street_address2: An optional secondary street address.
        county: The county for the delivery address.
        date: The date and time when the order was created.
        delivery_cost: The cost of delivery for the order.
        order_total: The total cost of the items in the order.
        grand_total: The total cost after applying discounts and delivery.
        original_bag: A JSON-like string representing original bag of items.
        stripe_pid: The payment identifier from Stripe.
        discount: The discount applied to the order.
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.

        Returns:
            str: A unique order number.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the order totals each time a line item is added,
        accounting for discount costs.

        This method calculates the order total, applies any discounts,
        and updates the grand total accordingly.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )

        # Define the discount threshold and percentage
        discount_threshold = settings.DISCOUNT_THRESHOLD
        discount_percentage = settings.DISCOUNT_PERCENTAGE

        if self.order_total >= discount_threshold:
            self.discount = self.order_total * discount_percentage / 100
        else:
            self.discount = 0

        # Calculate grand total after applying discount
        self.grand_total = self.order_total - self.discount
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the order.

        Returns:
            str: The order number.
        """
        return self.order_number

    def get_meeting_links(self):
        """
        Retrieve meeting links for all products in the order.

        Returns:
            list: A list of meeting links for each product in the order.
        """
        return [item.product.meeting_link for item in self.lineitems.all()]


class OrderLineItem(models.Model):
    """
    Model representing a line item in an order.

    Attributes:
        order: The order to which this line item belongs.
        product: The product associated with this line item.
        quantity: The quantity of the product ordered.
        lineitem_total: The total cost for this line item.
    """

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)

    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        based on product price and quantity, and update the order total.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the line item.

        Returns:
            str: A description of the line item including SKU and order number.
        """
        return f"SKU {self.product.sku} on order {self.order.order_number}"
