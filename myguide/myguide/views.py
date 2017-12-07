from django.views.generic import TemplateView
from django.views.generic.edit import FormView

class HomePageView(TemplateView):
  template_name = 'myguide/home.html'

class RegisterView(TemplateView):
  template_name = 'myguide/register.html'

class LoginView(TemplateView):
  template_name = 'myguide/login.html'