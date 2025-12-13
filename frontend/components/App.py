from reactpy import component, html, hooks
from frontend.pages.login import LoginPage
from frontend.pages.user_dashboard import UserDashboardPage
from frontend.pages.package import PackagePage

@component
def App():
    path = hooks.use_location().pathname   
    if path == "/login/":
        return LoginPage()

    if path.startswith("/dashboard"):
        return UserDashboardPage()

    if path.startswith("/packages"):
        return PackagePage()

    return html.h1("404 Page Not Found")
