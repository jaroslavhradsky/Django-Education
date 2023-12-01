from products.models import Product
from users.models import User

from .testcases import SplinterTestCase


class AddToCartPageTest(SplinterTestCase):

    def test_unauthenticated_user(self):
        user = User.objects.create_user(
            email="roselyn@wheeler.com",
            password="password",
        )
        duck = Product.objects.create(
            name="duck",
            description="Adorable rubber duck",
            price=1.25,
        )

        # User visits duck page and adds item to cart
        self.visit(duck.get_absolute_url())
        assert self.browser.is_text_not_present("Logout")
        assert not self.browser.is_element_present_by_text("Add to Cart")
        self.browser.find_by_text("Login to Add to Cart").click()
        self.browser.fill("username", user.email)
        self.browser.fill("password", "password")
        self.browser.find_by_css("button[type=submit]").click()
        self.assertEqual(self.browser.url, duck.get_absolute_url())
        assert self.browser.is_element_present_by_text("Add to Cart")
        assert self.browser.is_text_present("Logout")

    def test_user_adds_multiple_items_to_cart(self):
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

        # User logs-in
        user = User.objects.create_user(
            email="roselyn@wheeler.com",
            password="password",
        )
        self.login(user.email, "password")

        # User visits duck page and adds item to cart
        self.visit(duck.get_absolute_url())
        self.browser.find_by_text("Add to Cart").click()
        assert self.browser.is_text_present("Your Shopping Cart")
        assert self.browser.is_text_present("duck")
        assert self.browser.is_text_not_present("mouse")

        # User's cart state is correct
        self.assertEqual(user.cart.items.count(), 1)
        self.assertEqual(user.cart.items.get().product, duck)
        self.assertEqual(user.cart.items.get().quantity, 1)

        # User visits mouse page and adds item to cart, twice
        self.visit(mouse.get_absolute_url())
        self.browser.find_by_text("Add to Cart").click()
        assert self.browser.is_text_present("Your Shopping Cart")
        assert self.browser.is_text_present("mouse")
        assert self.browser.is_text_present("duck")
        self.visit(mouse.get_absolute_url())
        self.browser.find_by_text("Add to Cart").click()

        # User's cart state is correct
        self.assertEqual(user.cart.items.count(), 2)
        duck_item = user.cart.items.get(product=duck)
        mouse_item = user.cart.items.get(product=mouse)
        self.assertEqual(duck_item.quantity, 1)
        self.assertEqual(mouse_item.quantity, 2)
