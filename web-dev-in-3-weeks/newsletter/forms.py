from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """Form for newsletter subscriber."""
    class Meta:
        model = Subscriber
        fields = ["name", "email"]
