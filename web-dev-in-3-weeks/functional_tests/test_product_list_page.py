from products.models import Product

from .testcases import SplinterTestCase


class ProductListPageTest(SplinterTestCase):

    def test_all_products_shown(self):
        duck = Product.objects.create(
            name="duck",
            description="Adorable rubber duck",
            price=1.25,
        )
        mouse = Product.objects.create(
            name="mouse",
            description="A computer mouse",
            price=8.50,
        )
        self.visit("products:list")
        self.assertEqual(self.browser.status_code, 200)
        assert self.browser.is_text_present(duck.name)
        assert self.browser.is_text_present(duck.description)
        assert self.browser.is_text_present(f"{duck.price}")
        assert self.browser.is_text_present(mouse.name)
        assert self.browser.is_text_present(mouse.description)
        assert self.browser.is_text_present(f"{mouse.price}")
