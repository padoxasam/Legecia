from django.shortcuts import render
from frontend.components.App import App  # Important

def reactpy(component_path):
    def view(request, *args, **kwargs):
        return render(
            request,
            "frontend/reactpy_base.html",
            {
                "component": component_path,
                
            }
        )
    return view
