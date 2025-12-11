# frontend/views.py
from django.shortcuts import render

def user_dashboard(request):
    return render(request, "frontend/reactpy_base.html", {"component": "frontend.pages.user_dashboard.UserDashboardPage"})
