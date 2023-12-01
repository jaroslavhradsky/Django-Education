from django.test import TestCase

from products.models import Product
from users.models import User
from .models import Cart


class CartModelTest(TestCase):

    """Unit tests for Cart model."""

    def test_creation(self):
        user = User.objects.create(email="test@email.com", password="12345")
        cart = Cart.objects.create(user=user)
        self.assertEqual(cart.user, user)

    def test_string_representation(self):
        user = User.objects.create(email="test@email.com", password="12345")
        cart = Cart.objects.create(user=user)
        self.assertEqual(str(cart), "Cart for test@email.com")


class CartItemModelTest(TestCase):

    """Unit tests for CartItem model."""

    def test_creation_two_items(self):
        user = User.objects.create(email="test@email.com", password="12345")
        cart = Cart.objects.create(user=user)
        duck = Product.objects.create(
            name="duck",
            description="Adorable rubber duck",
            price=1,
        )
        cart.items.create(product=duck, quantity=1)
        self.assertEqual(cart.items.get().product, duck)

    def test_string_representations_of_two_items(self):
        user = User.objects.create(email="test@email.com", password="12345")
        cart = Cart.objects.create(user=user)
        duck = Product.objects.create(
            name="duck",
            description="Adorable rubber duck",
            price=5,
        )
        mouse = Product.objects.create(
            name="mouse",
            description="A plain computer mouse",
            price=2,
        )
        cart.items.create(product=duck, quantity=2)
        cart.items.create(product=mouse, quantity=1)
        self.assertEqual(
            {str(item) for item in user.cart.items.all()},
            {"duck (x2)", "mouse (x1)"},
        )
