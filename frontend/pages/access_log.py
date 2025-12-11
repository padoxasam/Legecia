from reactpy import component,html,hooks
from reactpy_django.hooks import use_query
from frontend.components.layout import Layout
from frontend.components.access_log_row import AccessLogRow
API_LOGS_URL='http://127.0.0.1:8000/api/access-logs/'
@component
def AccessLogsPage():
    logs,set_logs=hooks.use_state([])
    query=use_query
    async def fetch_logs():
        res=await query.get(API_LOGS_URL)
        if res.ok:
            set_logs(await res.json())
    hooks.use_effect(lambda:fetch_logs(),[])
    return (
        html.div(
            {"style": {"padding": "30px", "color": "#cce7ff", "fontFamily": "Orbitron"}},
            html.h1({"style": {"color": "#00eaff"}}, "🛡 Access Logs"),

            html.table(
                {"style": {
                    "width": "100%",
                    "borderCollapse": "collapse",
                    "marginTop": "25px",
                    "backgroundColor": "#111",
                    "color": "#fff",
                }},
                html.thead(
                    html.tr(
                        {"style": {"backgroundColor": "#022831"}},
                        *[html.th(
                                {"style": {"padding": "12px", "border": "1px solid #00eaff"}},
                                col
                            )
                            for col in [
                                "IP", "Device", "Login Time", "Logout", "Success", "Failure Msg"]])),
                    html.tbody(
                    *[AccessLogRow(log) for log in logs]))))
