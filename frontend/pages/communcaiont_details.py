from reactpy import component,html,hooks
from frontend.components.layout import Layout
from frontend.components.neon import TerminalHeader,NeonButton,NeonCard
from reactpy_django.hooks import use_query
API_DETAIL = "http://127.0.0.1:8000/api/communication/"

@component
def CommuncationDetailsPage(comm_id):
    data,set_data=hooks.use_state(None)
    query=use_query
    async def load():
        r=await query.get(f'{API_DETAIL}{comm_id}/')
        if r.ok:
            set_data(await r.json())
    hooks.use_effect(lambda:load(),[])
    if not data:
        return Layout(html.div('LOADING .....'))
    return Layout(
        html.div({"style": {"padding": "20px"}},
            TerminalHeader("COMMUNICATION DETAILS", f"Record #{comm_id}"),

            NeonCard([
                html.h3(data["relationship"]),
                html.p(f"User Email: {data['us_email']}"),
                html.p(f"Bene Email: {data['be_email']}"),

                html.p(f"Primary: {data['com_m1']}"),
                html.p(f"Secondary: {data.get('com_m2', 'None')}"),
                html.p(f"Visibility (User): {'🟢 Public' if data['is_user_public'] else '🔴 Private'}"),
                html.p(f"Visibility (Beneficiary): {'🟢 Public' if data['is_bene_public'] else '🔴 Private'}"),

                NeonButton("Edit", on_click=lambda e, cid=comm_id: go_edit(cid)),
                NeonButton("Back", on_click=lambda e: go_list()),
            ])
        )
    )
        
async def go_edit(comm_id):
    from reactpy_django.hooks import use_websocket
    webs=await use_websocket()
    await webs.exec(f'window.location.href="/communcation/{comm_id}/edit/";')
async def go_list():
        
        from reactpy_django.hooks import use_websocket
        webs=await use_websocket()
        await webs.exec("window.location.href = '/communication/';")



 