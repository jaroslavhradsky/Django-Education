from django.test import TestCase

from .forms import SubscriberForm
from .models import Subscriber


class SubscriberModelTests(TestCase):

    """Tests for Subscriber model."""

    def test_creation(self):
        """Create a save a valid Subscriber."""
        name = "Mae Mahoney"
        email = "mae@mahoney.name"
        subscriber = Subscriber(name=name, email=email)
        subscriber.save()
        self.assertEqual(subscriber.name, name)
        self.assertEqual(subscriber.email, email)

    def test_string_representation(self):
        """Check Subscriber string representation."""
        name = "Mary Sutton"
        email = "mary@sutton.name"
        subscriber = Subscriber(name=name, email=email)
        subscriber.save()
        self.assertEqual(str(subscriber), email)


class SubscriberFormTest(TestCase):

    """Tests for SubscriberForm."""

    def test_empty(self):
        form = SubscriberForm()
        self.assertEqual(form.data, {})
        self.assertFalse(form.is_valid())

    def test_name_but_no_email(self):
        data = {'name': "Mae Mahoney"}
        form = SubscriberForm(data)
        self.assertEqual(form.data, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            "email": ["This field is required."],
        })

    def test_email_but_no_name(self):
        data = {'email': "mae@mahoney.com"}
        form = SubscriberForm(data)
        self.assertEqual(form.data, data)
        self.assertTrue(form.is_valid())

    def test_email_and_name(self):
        data = {'email': "mae@mahoney.com", 'name': "Mae Mahoney"}
        form = SubscriberForm(data)
        self.assertEqual(form.data, data)
        self.assertTrue(form.is_valid())

    def test_save(self):
        data = {'email': "mae@mahoney.com", 'name': "Mae Mahoney"}
        form = SubscriberForm(data)
        self.assertTrue(form.is_valid())
        subscriber = form.save()
        self.assertEqual(subscriber.name, data['name'])
        self.assertEqual(subscriber.email, data['email'])
