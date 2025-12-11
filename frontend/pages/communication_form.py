from reactpy import component,html,hooks
from frontend.components.layout import Layout
from frontend.components.neon import TerminalHeader,NeonButton
from reactpy_django.hooks import use_query
API_CREATE = "http://127.0.0.1:8000/api/communication/create/"
API_UPDATE = "http://127.0.0.1:8000/api/communication/update/"
@component
def CommunicationFormPage(comm_id=None):
    form,set_form=hooks.use_state({"us_email": "",
        "be_email": "",
        "relationship": "",
        "com_m1": "",
        "com_m2": "",
        "additional_comments": "",})
    query=use_query
    async def load():
        if comm_id:
            r= await query.get(f'http://127.0.0.1:8000/api/communication/{comm_id}/')
            if r.ok:
                set_form(await r.json())
        hooks.use_effect(lambda:load(),[])
        async def handle_submit(event):
            event.prevent_default()
            endpoint=API_UPDATE if comm_id else API_CREATE
            r=await query.post(endpoint,json=form)
            if r.ok:
                await redirect_list()
        return Layout(
        html.div({"style": {"padding": "25px", "maxWidth": "500px", "margin": "auto"}},
            TerminalHeader("Communication Setup", "Define how you wish to be contacted"),

            html.form(
                {"onSubmit": handle_submit},
                html.label("User Email"),
                html.input({
                    "type": "email",
                    "value": form["us_email"],
                    "onChange": lambda e: set_form({**form, "us_email": e["target"]["value"]})
                }),
                html.br(),

                html.label("Beneficiary Email"),
                html.input({
                    "type": "email",
                    "value": form["be_email"],
                    "onChange": lambda e: set_form({**form, "be_email": e["target"]["value"]})
                }),
                html.br(),

                html.label("Relationship"),
                html.input({
                    "type": "text",
                    "value": form["relationship"],
                    "onChange": lambda e: set_form({**form, "relationship": e["target"]["value"]})
                }),
                html.br(),

                html.label("Primary Contact Method"),
                html.input({
                    "type": "text",
                    "value": form["com_m1"],
                    "onChange": lambda e: set_form({**form, "com_m1": e["target"]["value"]})
                }),
                html.br(),

                html.label("Secondary Contact Method"),
                html.input({
                    "type": "text",
                    "value": form["com_m2"],
                    "onChange": lambda e: set_form({**form, "com_m2": e["target"]["value"]})
                }),
                html.br(),

                html.label("Additional Comments"),
                html.textarea({
                    "value": form["additional_comments"],
                    "onChange": lambda e: set_form({**form, "additional_comments": e["target"]["value"]})
                }),
                html.br(),

                NeonButton("Save Communication Means"),
            ),
        )
    )
async def redirect_list():
    from reactpy_django.hooks import use_websocket
    webs=await use_websocket()
    await webs.exec('window.location.href="/communication/";')
    
