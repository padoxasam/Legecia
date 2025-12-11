from reactpy import component,html,hooks
from frontend.components.layout import Layout
from frontend.components.neon import NeonCard,NeonButton,TerminalHeader
from reactpy_django.hooks import use_query

API_LIST='"http://127.0.0.1:8000/api/communication/"'
API_TOGGLE_USER = 'http://127.0.0.1:8000/api/communication/toggle-user/' 
API_TOGGLE_BENE = 'http://127.0.0.1:8000/api/communication/toggle-bene/'

@component
def CommunicationListPage():
    commin,set_commin=hooks.use_State([])
    query=use_query
    async def load ():
        try:
            r=await query.get(API_LIST)
            if r.ok:
                set_commin(await r.json())
        except:
            pass
    hooks.use_effect(lambda:load(),[])
    async def toggle_user(commin_id):
        await query.post(API_TOGGLE_USER,json={'id':commin_id})
        await load()
    async def toggle_bene(commin_id):
        await query.post(API_TOGGLE_BENE, json={"id": commin_id})
        await load()
    
    return Layout(
        html.div(
            {"style": {"padding": "20px"}},
            TerminalHeader("COMMUNICATION CENTER — Neon Cyber Panel", "Visibility · Contact Methods · Relationship Map"),

            html.div(
                {"style": {"display": "grid", "gridTemplateColumns": "repeat(auto-fill,minmax(350px,1fr))", "gap": "18px"}},
                *[
                    NeonCard([
                        html.h3(c["relationship"]),
                        html.p(f"User Email: {c['us_email']}"),
                        html.p(f"Bene Email: {c['be_email']}"),
                        html.div({"style": {"marginTop": "10px"}},
                            html.p(f"User Visibility: {'🟢 Public' if c['is_user_public'] else '🔴 Private'}"),
                            NeonButton(
                                "Toggle User Visibility",
                                on_click=lambda e, cid=c["comm_id"]: toggle_user(cid)
                            ),
                        ),
                        html.br(),

                        html.div(
                            html.p(f"Bene Visibility: {'🟢 Public' if c['is_bene_public'] else '🔴 Private'}"),
                            NeonButton(
                                "Toggle Beneficiary Visibility",
                                on_click=lambda e, cid=c["comm_id"]: toggle_bene(cid)
                            ),
                        ),

                        html.br(),
                        NeonButton("View Details", on_click=lambda e, cid=c["comm_id"]: open_details(cid)),
                    ])
                    for c in commin ]),))
async def open_details(commin_id):
    from reactpy_django.hooks import use_websocket
    webs=await use_websocket
    await webs.exec(f"window.location.href = '/communication/{commin_id}/';")
