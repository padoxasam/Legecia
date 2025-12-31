"""
URL configuration for DJA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include,re_path
from django.http import HttpResponse
from django.views.generic import TemplateView

def home(request):
    return HttpResponse("Welcome! ya 7g")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("user_registration.urls")),
    path('',include('frontend.urls')),
    path('api/package/',include('package.urls')),
    path("api/log/", include("log.urls")),
    path('api/milestone/',include('milestone.urls')),
    path('api/supervision/',include('supervised.urls')),
    path('api/Notification/',include('Notification.urls')),
    path('api/access/',include('access.urls')),
    path('api/explorer/',include('explorer.urls')),
    path('api/credentials/',include('credentials.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),




]
