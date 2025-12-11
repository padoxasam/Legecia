from reactpy import component,html,hooks
from reactpy_django.hooks import use_query
from frontend.components.layout import Layout
from frontend.components.notification_card import NotificationCard
API_NOTIFICATION_URL='http://127.0.0.1:8000/api/notifications/'
@component
def NotificationPage():
    notification,set_notification=hooks.use_state([])
    query=use_query
    async def fetch_notification():
        res=await query.get(API_NOTIFICATION_URL)
        if res.ok:
            data=await res.json()
            set_notification(data)
    hooks.use_effect(lambda:fetch_notification(),[])
    return Layout(
        html.div(
            {"style": {
                "padding": "25px",
                "color": "#e0e0ff",
                "fontFamily": "Orbitron",
            }},
            html.h1({"style": {"color": "#00eaff"}}, "🔔 Notifications Center"),

            html.div(
                {"style": {
                    "marginTop": "25px",
                    "display": "flex",
                    "flexDirection": "column",
                    "gap": "15px",
                }},
                *[NotificationCard(n) for n in notification]
            )
        ))
        