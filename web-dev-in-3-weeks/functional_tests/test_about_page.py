from .testcases import SplinterTestCase


class AboutPageTest(SplinterTestCase):

    def test_correct_status_and_page_content(self):
        self.visit("about")
        self.assertEqual(self.browser.status_code, 200)
        assert self.browser.is_text_present('We were founded in 2022')
