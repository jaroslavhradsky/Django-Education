from .testcases import SplinterTestCase

from users.models import User


class NavbarTest(SplinterTestCase):

    def test_clicking_about_link(self):
        """Test About link URL and active state work correctly."""
        self.visit("home")  # Visit homepage
        about_link = self.browser.find_by_text("About")
        assert not about_link.has_class("active")  # About link isn't active
        about_link.click()  # Click About link
        self.assertEqual(self.browser.url, self.reverse("about"))
        assert not about_link.has_class("active")  # About link is active

    def test_clicking_newsletter_link(self):
        """Test Newsletter link URL and active state work correctly."""
        self.visit("home")  # Visit homepage
        newsletter_link = self.browser.find_by_text("Newsletter")
        assert not newsletter_link.has_class("active")  # Link isn't active
        newsletter_link.click()  # Click link
        self.assertEqual(
            self.browser.url,
            self.reverse("newsletter:subscribe"),
        )
        assert not newsletter_link.has_class("active")  # Link is active

    def test_clicking_cart_link(self):
        """Test Cart link URL and active state work correctly."""
        user = User.objects.create_user(email="tom@chan.com", password="1234")
        self.visit("home")  # Visit homepage
        assert not self.browser.is_element_present_by_text("Cart")  # No link
        self.login(user.email, "1234")
        cart_link = self.browser.find_by_text("Cart")
        assert not cart_link.has_class("active")  # Cart link isn't active
        cart_link.click()  # Click Cart link
        self.assertEqual(self.browser.url, self.reverse("carts:cart"))
        assert not cart_link.has_class("active")  # Cart link is active
