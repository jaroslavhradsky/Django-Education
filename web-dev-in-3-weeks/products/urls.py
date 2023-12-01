from django.urls import path

from .views import ProductDetailView, ProductListView

app_name = 'products'

urlpatterns = [
    path(
        'products/<int:product_id>/',
        ProductDetailView.as_view(),
        name='detail',
    ),
    path('products/', ProductListView.as_view(), name='list'),
]
