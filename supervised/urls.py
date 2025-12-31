from django.urls import path
from .views import CreateSupervision,SendSupervisionRequest,BeneficiaryViewSupevision

urlpatterns=[path('create/',CreateSupervision.as_view,name='Supervision_Create'),
             path('send,<int:supervision_id>/',SendSupervisionRequest.as_view(),name='Supervision send'),
             path('Beneficiary/<int:superivison_id>/',BeneficiaryViewSupevision.as_view(),name='Supervision view for bene'),


]