from reactpy import component,html,hooks
from reactpy_django.hooks import use_query
from frontend.components.neon import NeonButton,NeonCard,TerminalHeader,Metric
API_USERS='/api/users/list/'
API_BENEFICIARIES='/api/beneficiary/list/'
API_PACKAGES='/API/PACKAGES/MY-PACKAGES/'.lower()
API_REQEUST='/api/sueprivsed/request/'

@component
def RequestSupervisionPage():
    users,set_susers=hooks.use_state([])
    bene,set_bene=hooks.use_state([])
    packages,set_packages=hooks.use_State([])
    selected_user,set_selected_user=hooks.use_state('')
    selected_bene,set_selected_bene=hooks.use_state('')
    selected_package,set_selected_pacakge=hooks.use_State('')
    expiry,set_expiry=hooks.use_state('')
    message,set_message=hooks.use_state('')
    query=use_query
    async def load():
        u=await query.get(API_USERS)
        if u.ok:
            set_susers(await u.json())
        b=await query.get(API_BENEFICIARIES)
        if b.ok:
            set_bene(await b.json())
        pack=await query.get(API_PACKAGES)
        if pack.ok:
            set_packages(await pack.json())
    hooks.use_effect(lambda:load(),[])
    async def send_request():
        r=await query.post(API_REQEUST,json={'Package':selected_package,
                                             'Beneficiary':selected_bene,
                                             'Guardian': selected_user,
                                             'Expiry':expiry})
        if r.ok:
            set_message('Supervision Reuqest Sent Successfully !')
        else:
            set_message('Failed To Send Reuqest')
    return html.div(
        {"style": {"padding": "20px", "color": "#fff", "background": "#0a0f1a"}},
        TerminalHeader("REQUEST SUPERVISION", "Create supervision link between user → bene → guardian"),
        NeonCard([
            html.h3("Select Package"),
            html.select(
                {"value": selected_package, "onChange": lambda e: set_selected_pacakge(e["target"]["value"])},
                html.option({"value": ""}, "Choose…"),
                *[html.option({"value": p["id"]}, p["name"]) for p in packages],
            ),

            html.h3("Select Beneficiary"),
            html.select(
                {"value": selected_bene, "onChange": lambda e: set_selected_bene(e["target"]["value"])},
                html.option({"value": ""}, "Choose…"),
                *[html.option({"value": b["id"]}, b["name"]) for b in bene],
            ),

            html.h3("Select Guardian"),
            html.select(
                {"value": selected_user, "onChange": lambda e: set_selected_user(e["target"]["value"])},
                html.option({"value": ""}, "Choose…"),
                *[html.option({"value": u["id"]}, u["name"]) for u in users],
            ),

            html.h3("Expiry Date"),
            html.input({
                "type": "date",
                "value": expiry,
                "onChange": lambda e: set_expiry(e["target"]["value"])
            }),html.div({"style": {"marginTop": "20px"}},
                     NeonButton("Send Request", on_click=lambda e: send_request())),html.p({"style": {"marginTop": "15px", "color": "#79d3fa"}}, message)]))