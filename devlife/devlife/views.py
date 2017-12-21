from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
 
class HomePageView(TemplateView):
  def get(self, request):
    if request.user.is_authenticated:
      return redirect('/dashboard')
    else:
      return render(request,'devlife/home.html', {})

class RegisterView(TemplateView):
  def get(self, request):
    if request.user.is_authenticated:
      return redirect('/dashboard')
    else:
      return render(request,'devlife/register.html', {})

class LoginView(TemplateView):
  def get(self, request):
    if request.user.is_authenticated:
      return redirect('/dashboard')
    else:
      return render(request,'devlife/login.html', {})

class DashboardView(TemplateView):
  def get(self, request):
    if request.user.is_authenticated:
      return render(request, "devlife/dashboard.html", {})
    else:
      return redirect("/login")

def logoutView(request):
  logout(request)
  return redirect("/")
