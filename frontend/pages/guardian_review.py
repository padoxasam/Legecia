from frontend.components.neon import TerminalHeader,NeonCard,NeonButton
from reactpy_django.hooks import use_query
from reactpy import component,html,hooks
API_GET='/API/SUPERVISED/{id}/'.lower()

API_Action='/api/supervised/{id}/{action}/'
@component
def GuardianReviewPage(package_id):
    data,set_data=hooks.use_state(None)
    loading,set_loading=hooks.use_State(True)
    query=use_query
    async def load():
        set_loading(True)
        r=await query.get(API_GET.format(id=package_id))
        if r.ok:
            set_data(await r.json())
        set_loading(False)
    async def take_action(action):
        r=await query.post(API_Action.format(id=package_id,action=action),json={})
        if r.ok:
            await load()
    hooks.use_effect(lambda: load(),[])
    if loading :
        return html.div('loading Review Page ......')
    if not data:
        return html.div('Package Not Found !')
    return html.div(
        {
            "style": {
                "padding": "20px",
                "color": "#fff",
                "background": "#0a0f1a",
                "fontFamily": "monospace",
            }
        },
        TerminalHeader("GUARDIAN — SUPERVISION REVIEW", "Approve or reject package supervision"),
        NeonCard([
            html.h2(f"Package: {data.get('package_name')}"),
            html.p(f"Requested by user: {data.get('requested_by')}"),
            html.p(f"Beneficiary: {data.get('beneficiary_name')}"),
            html.p(f"Current status: {data.get('guardian_status')}"),
            html.p(f"Expires on: {data.get('guardian_expiry')}"),
            html.div(
                {"style": {"marginTop": "18px", "display": "flex", "gap": "15px"}},
                NeonButton("Approve", on_click=lambda e: take_action("approve")),
                NeonButton("Reject", on_click=lambda e: take_action("reject")),
                NeonButton("Back", on_click=lambda e: go_back()),
            )
        ])
    )
async def go_back():
    from reactpy_django.hooks import use_websocket
    webs=await use_websocket()
    await webs.exec('window.history.back();')

    