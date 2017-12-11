from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect

class HomePageView(TemplateView):
  template_name = 'devlife/home.html'

class RegisterView(TemplateView):
  template_name = 'devlife/register.html'

class LoginView(TemplateView):
  template_name = 'devlife/login.html'

def logoutView(request):
  logout(request)
  return redirect("/")
