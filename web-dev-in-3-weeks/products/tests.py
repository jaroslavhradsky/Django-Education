from django.test import TestCase

from .models import Product


class ProductModelTests(TestCase):

    """Tests for Product model."""

    def test_creation(self):
        """Create a save a valid Product."""
        duck = Product(
            name="duck",
            description="Adorable rubber duck",
            price=1,
        )
        duck.save()
        self.assertEqual(duck.name, "duck")
        self.assertEqual(duck.description, "Adorable rubber duck")
        self.assertEqual(duck.price, 1)

    def test_string_representation(self):
        """Check product string representation."""
        duck = Product(
            name="duck",
            description="Adorable rubber duck",
            price=1,
        )
        duck.save()
        self.assertEqual(str(duck), "duck")
