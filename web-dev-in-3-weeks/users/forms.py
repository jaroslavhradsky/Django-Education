from django import forms

from .models import User


class RegistrationForm(forms.ModelForm):
    """Form to register a new user."""

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "autofocus": True,
                "autocapitalize": "none",
                "autocomplete": "email",
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
