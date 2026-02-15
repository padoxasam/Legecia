from django.urls import path
from .views import LogListView, MyLogListView

urlpatterns = [
    path("", LogListView.as_view(), name="log-list"),
    path("my/", MyLogListView.as_view(), name="my-log-list"),
]
