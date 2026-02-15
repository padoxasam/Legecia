from django.urls import path
from .views import CreateSupervision, SendSupervisionRequest, BeneficiaryViewSupevision

urlpatterns = [
    path('create/', CreateSupervision.as_view(), name='supervision-create'),
    path('send/<int:supervision_id>/', SendSupervisionRequest.as_view(), name='supervision-send'),
    path('beneficiary/<int:superivision_id>/', BeneficiaryViewSupevision.as_view(), name='supervision-beneficiary-view'),
]
