from django.urls import path
from .views import PublicPackageListView,PublicPackageCreateView,PublicPackageDetailView


urlpatterns = [
    path("public/", PublicPackageListView.as_view(), name="public-packages"),
    path("public/create/", PublicPackageCreateView.as_view(), name="public-create"),
    path("public/<int:pk>/", PublicPackageDetailView.as_view(), name="public-detail"),
]
