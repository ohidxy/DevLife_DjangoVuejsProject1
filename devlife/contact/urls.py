from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^$', views.contact_page, name='contact_page'),
    url(r'^rest-api/$', views.ContactData.as_view(), name="contact_data_api"),  # this is for api only. it doesn't relate to any templates
    url(r'^rest-api/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view(), name="contact_detail"),  
]