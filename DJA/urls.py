from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_registration.urls')),
    path('api/core/', include('core.urls')),
    path('api/package/', include('package.urls')),
    path('api/log/', include('log.urls')),
    path('api/milestone/', include('milestone.urls')),
    path('api/supervision/', include('supervised.urls')),
    path('api/notification/', include('Notification.urls')),
    path('api/access/', include('access.urls')),
    path('api/explorer/', include('explorer.urls')),
    path('api/credentials/', include('credentials.urls')),
    path('api/communication/', include('communication.urls')),

    # React frontend catch-all (must be last)
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
