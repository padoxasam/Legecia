from django.urls import path
from django.views.generic import TemplateView

#from reactpy_django.http import ReactPyView
from frontend.pages.home import HomePage
urlpatterns=[
    path('',TemplateView.as_view(template_name="frontend/home.html"),name='view'),
    path('login/')
    ]