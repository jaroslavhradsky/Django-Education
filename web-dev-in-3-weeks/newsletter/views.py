from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from .forms import SubscriberForm
from .models import Subscriber


class NewsletterView(SuccessMessageMixin, CreateView):
    model = Subscriber
    form_class = SubscriberForm
    template_name = "newsletter.html"
    success_url = "/"
    success_message = "Thanks for signing up to our newsletter!"
