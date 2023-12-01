from django.urls import path
from .views import CartView, AddToCartView


app_name = 'carts'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add'),
]
