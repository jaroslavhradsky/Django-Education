from django.urls import path
from .views import NewsletterView

app_name = 'newsletter'
urlpatterns = [
    path('newsletter/', NewsletterView.as_view(), name='subscribe'),
]
