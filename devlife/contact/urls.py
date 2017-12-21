from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^$', views.contact_page, name='contact_page'),
    url(r'^api/$', views.contact_data, name="contact_data_api"),  # this is for api only. it doesn't relate to any templates
]