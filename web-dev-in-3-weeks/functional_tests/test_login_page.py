from users.models import User

from .testcases import SplinterTestCase


class LoginTest(SplinterTestCase):

    def test_incorrect_password(self):
        user = User.objects.create_user(
            email="kathleen@grenier.com",
            password="my secret password",
        )
        self.visit("home")  # Visit homepage
        self.browser.find_by_text("Login").click()  # Click Login
        self.browser.fill("username", user.email)
        self.browser.fill("password", "invalid")
        self.browser.find_by_css("button[type=submit]").click()
        self.assertEqual(self.browser.url, self.reverse("users:login"))
        assert self.browser.is_text_present(
            "Please enter a correct email address and password."
        )
        assert self.browser.is_text_not_present("Logout")
        assert self.browser.is_text_present("Login")

    def test_valid_login(self):
        user = User.objects.create_user(
            email="kathleen@grenier.com",
            password="my secret password",
        )
        self.visit("home")  # Visit homepage
        self.browser.find_by_text("Login").click()  # Click Login
        self.browser.fill("username", user.email)
        self.browser.fill("password", "my secret password")
        self.browser.find_by_css("button[type=submit]").click()
        self.assertEqual(self.browser.url, self.reverse("home"))
        assert self.browser.is_text_present("Logout")
        assert self.browser.is_text_not_present("Login")
