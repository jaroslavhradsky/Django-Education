from carts.models import Cart
from products.models import Product
from users.models import User

from .testcases import SplinterTestCase


class CartPageTest(SplinterTestCase):

    def test_unauthenticated(self):
        self.visit("carts:cart")
        self.assertEqual(
            self.browser.url,
            f"{self.reverse('users:login')}"
            + f"?next={self.reverse('carts:cart')}",
        )

    def test_no_cart_for_user(self):
        # User logs-in
        user = User.objects.create_user(
            email="roselyn@wheeler.com",
            password="password",
        )
        self.login(user.email, "password")

        # User visits cart page and sees nothing in cart
        self.visit("carts:cart")
        assert self.browser.is_text_present("Your Shopping Cart")
        assert self.browser.is_text_not_present("duck")
        assert self.browser.is_text_not_present("mouse")

    def test_user_cart_with_items(self):
        # User logs-in
        user = User.objects.create_user(
            email="roselyn@wheeler.com",
            password="password",
        )
        Cart.objects.create(user=user)
        self.login(user.email, "password")

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
        user.cart.items.create(product=duck, quantity=9)

        # User visits cart page and sees 1 product with quantity & cost
        self.visit("carts:cart")
        assert self.browser.is_text_present("Your Shopping Cart")
        assert self.browser.is_text_present("duck")
        assert self.browser.is_text_present("9")
        assert self.browser.is_text_present("1.25")
        assert self.browser.is_text_not_present("mouse")
        assert self.browser.is_text_not_present("7")
        assert self.browser.is_text_not_present("8.50")

        user.cart.items.create(product=mouse, quantity=7)

        # User visits cart page and sees 2 products
        self.visit("carts:cart")
        assert self.browser.is_text_present("Your Shopping Cart")
        assert self.browser.is_text_present("duck")
        assert self.browser.is_text_present("9")
        assert self.browser.is_text_present("1.25")
        assert self.browser.is_text_present("mouse")
        assert self.browser.is_text_present("7")
        assert self.browser.is_text_present("8.50")
