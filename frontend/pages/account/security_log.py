from reactpy import component, html, hooks
from frontend.components.layout import Layout
from frontend.components.neon import TerminalHeader, NeonCard
from reactpy_django.hooks import use_query
API_SECURITY_LOG='/api/credentialis/security-log'
@component
def SecurityLogPage():
    logs,set_logs=hooks.use_state([])
    query=use_query
    async def load():
        r=await query.get(API_SECURITY_LOG)
        if r.ok:
            set_logs(await r.json())
    hooks.use_effect(lambda:load(),[])
    return Layout(
        html.div(
            {"style": {"padding": "25px"}},
            TerminalHeader("SECURITY ACTIVITY", "Recent login attempts & system alerts"),

            html.div(
                {"style": {"display": "grid", "gap": "12px"}},
                *[
                    NeonCard([
                        html.h4(f"IP: {l.get('ip')}  —  {l.get('status')}"),
                        html.p(f"Timestamp: {l.get('time')}"),
                        html.p({"style": {"color": "#8899a6"}}, l.get("device")),
                    ])
                    for l in logs
                ]
            )
        )
    )
