from reactpy import component,html,hooks
from frontend.components.layout import Layout
from frontend.components.neon import NeonButton,TerminalHeader
from reactpy_django.hooks import use_query

API_CHANGE_PASSWORD ='/api/credentials/change-password/'
@component
def ChangePasswordPage():
    old_pass,set_old=hooks.use_state('')
    new_pass,set_new=hooks.use_state('')
    confirm_pass,set_confirm=hooks.use_state('')
    message,set_message=hooks.use_state('')
    query=use_query
    def handle_submit(event):
        event.prevent_default()
        if new_pass!=confirm_pass:
            set_message("Passwords Don't Match ❌ "  )
            return
        async def send ():
            r=await query.post(API_CHANGE_PASSWORD,json={'old_password':old_pass,'new_password':new_pass},)

            data=await r.json()
            set_message(data.get('message',''))
        return send
    return Layout(
        html.div(
            {
                "style": {
                    "padding": "25px",
                    "maxWidth": "500px",
                    "margin": "0 auto",
                    "color": "white",
                }
            },
            TerminalHeader("CHANGE PASSWORD", "High-security password update"),

            html.form(
                {"onSubmit": handle_submit},
                html.label("Old Password"),
                html.input({
                    "type": "password",
                    "value": old_pass,
                    "onChange": lambda e: set_old(e["target"]["value"])
                }),
                html.br(),

                html.label("New Password"),
                html.input({
                    "type": "password",
                    "value": new_pass,
                    "onChange": lambda e: set_new(e["target"]["value"])
                }),
                html.br(),
                 html.label("Confirm New Password"),
                html.input({
                    "type": "password",
                    "value": confirm_pass,
                    "onChange": lambda e: set_confirm(e["target"]["value"])
                }),
                html.br(),

                NeonButton("Update Password"),
            ),
            html.p(message),
        )
    )
    
    