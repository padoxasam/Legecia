from reactpy import component, html

@component
def HomePage():
    return html.div(
        html.h1("Welcome to Home Page"),
        html.ul(
            html.li(html.a("User Dashboard", href="/dashboard/user/")),
            html.li(html.a("Beneficiary Dashboard", href="/dashboard/beneficiary/")),
            html.li(html.a("Guardian Dashboard", href="/dashboard/guardian/")),
            html.li(html.a("Packages", href="/packages/")),
            html.li(html.a("Milestone", href="/milestone/")),
            html.li(html.a("Notification", href="/notification/")),))
