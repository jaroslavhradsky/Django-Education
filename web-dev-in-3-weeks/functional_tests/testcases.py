from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from splinter import Browser


class SplinterTestCase(StaticLiveServerTestCase):

    def setUp(self):
        super().setUp()
        self.browser = Browser("django")

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def reverse(self, url_name, *args, **kwargs):
        return reverse(url_name, args=args, kwargs=kwargs)

    def login(self, email, password):
        self.visit("users:login")
        self.browser.fill("username", email)
        self.browser.fill("password", password)
        self.browser.find_by_css("button[type=submit]").click()

    def visit(self, url_name, *args, **kwargs):
        if url_name.startswith("/") and not args and not kwargs:
            url = url_name
        else:
            url = self.reverse(url_name, *args, **kwargs)
        self.browser.visit(f"{self.live_server_url}{url}")
