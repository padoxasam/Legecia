from reactpy import component,html
def NotificationCard(notification):
    priority_color = {
        "Low": "#44ff44",
        "Medium": "#ffaa00",
        "High": "#ff4444",
        "Critical": "#ff0000",
    }.get(notification.get("priority"), "#ffffff")

    return html.div(
        {
            "style": {
                "border": f"2px solid {priority_color}",
                "padding": "15px",
                "borderRadius": "10px",
                "backgroundColor": "#0b0f1e",
                "boxShadow": f"0 0 12px {priority_color}",
                "fontFamily": "Orbitron",
            }},
        html.h3(
            {"style": {"marginBottom": "5px", "color": priority_color}},
            f"⚡ {notification.get('topic')}"
        ),
        html.p(
            {"style": {"marginBottom": "10px", "color": "#ccc"}},
            notification.get("message")
        ),
        html.span({"style": {"fontSize": "12px", "color": "#999"}},
                  f"At: {notification.get('created_at')}"),)