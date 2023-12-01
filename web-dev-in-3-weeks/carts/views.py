from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from carts.models import Cart
from products.models import Product


class CartView(LoginRequiredMixin, ListView):
    template_name = "cart.html"
    context_object_name = "items"

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.items.all()


class AddToCartView(LoginRequiredMixin, DetailView):
    http_method_names = ["post"]
    model = Product
    pk_url_kwarg = "product_id"

    def post(self, request, product_id):
        product = self.get_object()
        cart, created = Cart.objects.get_or_create(user=request.user)
        item, created = cart.items.get_or_create(
            product=product,
            defaults={'quantity': 1},
        )
        if not created:
            item.quantity += 1
            item.save()
        messages.success(request, f"Added {product.name} to cart")
        return redirect("carts:cart")
