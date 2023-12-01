from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'about.html'


class HomeView(TemplateView):
    template_name = 'home.html'
