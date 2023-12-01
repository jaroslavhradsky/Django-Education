from django.test import TestCase

from .forms import RegistrationForm
from .models import User


class UserModelTest(TestCase):

    """Unit tests for Custom User model."""

    def test_user_creation(self):
        """Create a valid user and save it."""
        email = 'test@email.com'
        password = '12345'
        user = User.objects.create(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.get_short_name(), email)
        self.assertEqual(user.get_full_name(), email)


class RegistrationFormTest(TestCase):

    """Tests for user RegistrationForm."""

    def test_empty(self):
        form = RegistrationForm()
        self.assertEqual(form.data, {})
        self.assertFalse(form.is_valid())

    def test_no_password(self):
        data = {"email": "eva@shae.com"}
        form = RegistrationForm(data)
        self.assertEqual(form.data, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            "password": ["This field is required."],
        })

    def test_no_email(self):
        data = {"password": "wall pet direct hiking"}
        form = RegistrationForm(data)
        self.assertEqual(form.data, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            "email": ["This field is required."],
        })

    def test_email_and_password(self):
        data = {"email": "eva@shae.com", "password": "wall pet direct hiking"}
        form = RegistrationForm(data)
        self.assertEqual(form.data, data)
        self.assertTrue(form.is_valid())

    def test_save_works(self):
        data = {"email": "eva@shae.com", "password": "wall pet direct hiking"}
        form = RegistrationForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.email, data["email"])
        self.assertTrue(user.check_password(data["password"]))

    def test_existing_user(self):
        data = {"email": "eva@shae.com", "password": "wall pet direct hiking"}
        User.objects.create(email=data["email"], password="")
        form = RegistrationForm(data)
        self.assertEqual(form.data, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            "email": ["User with this Email address already exists."],
        })
