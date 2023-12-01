from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import RegistrationForm


def logout_view(request):
    logout(request)
    return redirect("home")


class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/"
    success_message = "Thanks for creating an account!"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
