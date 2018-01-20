from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^$', views.todo_page, name='todo_page'),
    url(r'^rest-api/$', views.TodoData.as_view(), name="todo_api"), 
]