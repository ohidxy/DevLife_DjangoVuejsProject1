from django.conf.urls import url, include
from django.contrib import admin
from .views import HomePageView, RegisterView, LoginView, DashboardView, logoutView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    
    url(r'^logout/$', logoutView , name='logout'),

    url(r'^admin/', admin.site.urls),
    
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),

    url(r'^contact/', include('devlife.contact.urls')),
]
