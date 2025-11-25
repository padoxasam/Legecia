from django.urls import path
from .views import ProfileView, ProfileUpdateView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path('api/users/', include('user_registration.urls')),

    path('api/packages/', include('package.urls')),
    path('api/communication/',include('communication.urls')),
    
]
