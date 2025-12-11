from reactpy import component, html, hooks

@component
def Sidebar():
    expanded, set_expanded = hooks.use_state(False)
    links=[("Home", "/"),
        ("Packages", "/packages"),
        ("Milestone", "/milestone"),
        ("Notifications", "/notifications"),
        ("Switch Role", "/switch-role"),
        ("Account Settings", "/account/settings"),
        ('logout','/logout'),
        ('Request SSupervision','/request-supervision'),
        ('Review Supervision','/supervised-review'),]
    def toggle_milestone(event):
        set_expanded(not expanded)
    

    return html.div(
        {"style": {
                "width": "220px",
                "backgroundColor": "#0b0820",
                "color": "#e0e0ff",
                "padding": "20px",
                "minHeight": "100vh",
                "boxShadow": "0 0 18px rgba(0,255,230,0.15)"
            }
        },
       
        html.a({"href": "/", "style": nav_link()}, "Home"),
        html.a({"href": "/packages", "style": nav_link()}, "Packages"),
        html.div({"style": nav_link(), "onClick": toggle_milestone}, "Milestones ▾" if expanded else "Milestones ▸"),
        html.div(
            {"style": {"marginLeft": "15px", "display": "block" if expanded else "none", "transition": "0.3s"}},
            html.a({"href": "/milestones/", "style": sub_link()}, "• Milestone Overview"),
            html.a({"href": "/milestones/create", "style": sub_link()}, "• Create Milestone"),
            html.a({"href": "/milestones/upload", "style": sub_link()}, "• Upload Milestone"),
            html.a({"href": "/milestones/preview", "style": sub_link()}, "• Preview Milestone"),
        ),
        html.a({"href": "/notifications", "style": nav_link()}, "Notifications"),
        html.a({"href": "/switch-role", "style": nav_link()}, "Switch Role"),)


def nav_link():
    return {
        "display": "block",
        "margin": "12px 0",
        "padding": "8px",
        "cursor": "pointer",
        "color": "white",
        "textDecoration": "none",
        "borderRadius": "6px",
        "transition": "0.25s",
        "backgroundColor": "rgba(255,255,255,0.07)",}
def sub_link():
    return {
        "display": "block",
        "margin": "6px 0",
        "padding": "6px",
        "color": "#2fe0e9",
        "textDecoration": "none",
        "fontSize": "13px",
        "borderRadius": "4px",}
