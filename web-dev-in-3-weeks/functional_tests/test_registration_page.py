from users.models import User

from .testcases import SplinterTestCase


class RegisterTest(SplinterTestCase):

    def test_existing_user(self):
        user = User.objects.create_user(
            email="darnell@marsh.com",
            password="tuesday votes nickname wood",
        )
        self.visit("home")  # Visit homepage
        self.browser.find_by_text("Register").click()  # Click Register
        self.browser.fill("email", user.email)
        self.browser.fill("password", "tuesday votes nickname wood")
        self.browser.find_by_css("button[type=submit]").click()
        self.assertEqual(self.browser.url, self.reverse("users:register"))
        assert self.browser.is_text_present(
            "User with this Email address already exists."
        )
        assert self.browser.is_text_not_present("Logout")
        assert self.browser.is_text_present("Register")

    def test_valid_registration(self):
        self.visit("home")  # Visit homepage
        self.browser.find_by_text("Register").click()  # Click Register
        self.browser.fill("email", "darnell@marsh.com")
        self.browser.fill("password", "tuesday votes nickname wood")
        self.browser.find_by_css("button[type=submit]").click()
        self.assertEqual(self.browser.url, self.reverse("home"))
        assert self.browser.is_text_present("Logout")
        assert self.browser.is_text_not_present("Register")
