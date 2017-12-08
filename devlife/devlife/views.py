from django.views.generic import TemplateView
from django.views.generic.edit import FormView

class HomePageView(TemplateView):
  template_name = 'devlife/home.html'

class RegisterView(TemplateView):
  template_name = 'devlife/register.html'

class LoginView(TemplateView):
  template_name = 'devlife/login.html'