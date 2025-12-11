from reactpy import component, html, hooks
from frontend.components.layout import Layout
from frontend.components.neon import NeonButton, TerminalHeader
from reactpy_django.hooks import use_query
API_2FA='/API/CREDENTIALS/2FA'.lower() # kslt aktb  tany ;)
@component
def TwoFactorPage():
    enabled,set_enabled=hooks.use_state(False)
    message,set_message=hooks.use_state('')
    query=use_query
    async def load():
        r=await query.get(API_2FA)
        if r.ok:
            data=await r.json()
            set_enabled(data.get('enabled',False))

    hooks.use_effect(lambda:load(),[])
    def toggle(event):
        async def send():
            r=await query.post(API_2FA,json={'enable':not enabled})
            data=await r.json()
            set_message(data.get('message',''))
            set_enabled(not enabled)
        return send
    return Layout(
        html.div(
            {"style": {"padding": "25px"}},
            TerminalHeader("TWO-FACTOR AUTHENTICATION", "Add an extra layer of security"),

            html.h3(f"2FA Status: {' Enabled 🟢' if enabled else ' Disabled 🟢'}"),
            NeonButton("Toggle 2FA", on_click=toggle),
            html.p(message)
        )
    )
    


