from django.urls import path
from .views import PackageListCreateView, PackageDetailsView

app_name='package'
urlpatterns=[ path('',PackageListCreateView.as_view(),name='package-list-create'),
             path('<int:pk>/',PackageDetailsView.as_view(),name='package details'),
                  

]
