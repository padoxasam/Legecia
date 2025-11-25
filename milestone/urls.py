from django.urls import path
from .views import UserCreateMilestone,BeneficiaryUploadMilestone,MilestoneDetails

urlpatterns=[path('create',UserCreateMilestone.as_view(),name='Milestone-create'),
             path('upload/<int:milestone_id>/',BeneficiaryUploadMilestone.as_view(),name='milestone-upload'),
             path('<int:milestone_id>/',MilestoneDetails.as_view(),name='milestone-details'),



]