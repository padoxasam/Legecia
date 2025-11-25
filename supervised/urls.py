from django.urls import path
from .views import CreateSupervision,GuardianUpdateSupervision,BeneficiaryViewSupevision

urlpatterns=[path('create/',CreateSupervision.as_view,name='Supervision_Create'),
             path('Guardian,<int:supervision_id>/',GuardianUpdateSupervision.as_view(),name='Supervision Update'),
             path('Beneficiary/<int:superivison_id>/',BeneficiaryViewSupevision.as_view(),name='Supervision view for bene'),


]