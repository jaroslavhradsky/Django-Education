from newsletter.models import Subscriber

from .testcases import SplinterTestCase


class NewsletterPageTest(SplinterTestCase):

    def test_correct_status_and_page_content(self):
        self.visit("newsletter:subscribe")
        self.assertEqual(self.browser.status_code, 200)
        assert self.browser.is_text_present("Sign up for our newsletter")

    def test_valid_newsletter_signup(self):
        # Navigate to newsletter page
        email = "bryce@tyree.com"
        self.visit("newsletter:subscribe")

        # Enter email and submit form
        self.browser.fill("email", email)
        self.browser.find_by_css("button[type=submit]").click()

        # Subscriber created
        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertEqual(Subscriber.objects.get().email, email)

        # See success message
        assert self.browser.is_text_present(
            "Thanks for signing up to our newsletter!"
        )
