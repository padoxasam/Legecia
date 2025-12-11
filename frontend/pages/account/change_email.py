from reactpy import component, html, hooks
from frontend.components.layout import Layout
from frontend.components.neon import NeonButton, TerminalHeader
from reactpy_django.hooks import use_query

API_CHANGE_EMAIL = "/api/credentials/change-email/"
@component
def ChageEmailPage():
    email,set_email=hooks.use_state('')
    message,set_message=hooks.use_state('')
    query=use_query
    def Submit(event):
        event.prevent_default()
        async def call():
            r=await query.post(API_CHANGE_EMAIL,json={'email':email})
            data=await r.json()
            set_message(data.get('message',''))
        return call
    return Layout(
        html.div(
            {"style": {"padding": "25px", "maxWidth": "450px", "margin": "0 auto"}},
            TerminalHeader("CHANGE EMAIL", "Update your login email"),

            html.form(
                {"onSubmit": Submit},
                html.label("New Email"),
                html.input({
                    "type": "email",
                    "value": email,
                    "onChange": lambda e: set_email(e["target"]["value"])
                }),
                html.br(),
                NeonButton("Update Email")
            ),
            html.p(message)
        )
    )
    
