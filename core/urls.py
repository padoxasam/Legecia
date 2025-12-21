from django.urls import path
from .views import (
    CoreProfileView,
    UserDashboardView,
    BeneficiaryDashboardView,
    GuardianDashboardView,
)

urlpatterns = [
    path('profile/', CoreProfileView.as_view()),

    # Dashboards
    path('dashboard/user/', UserDashboardView.as_view()),
    path('dashboard/beneficiary/', BeneficiaryDashboardView.as_view()),
    path('dashboard/guardian/', GuardianDashboardView.as_view()),
]
