from django.db import models


class Cart(models.Model):
    """Model representing a shopping cart."""

    user = models.OneToOneField(
        "users.User",
        unique=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    """Model representing a single item in a shopping cart."""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.product} (x{self.quantity})"
