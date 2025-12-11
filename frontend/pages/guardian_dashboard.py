from reactpy import component,html,hooks
from frontend.components.neon import TerminalHeader,NeonButton,NeonCard,Metric
from reactpy_django.hooks import use_query
from frontend.components.guardian_toolbar import GuardianToolBar
from frontend.components.Supervision_card import SupervisionCard

API_SUPERVISED='/api/supervised/'
@component
def GuardianDashboardPage():
    style=style={
        "padding": "16px",
        "background": "#0DCC56",
        "color": "#fff",
        "fontFamily": "sans-serif"}
    supervised,set_supervised=hooks.use_state([])
    loading,set_loading=hooks.use_state(True)
    message, set_message = hooks.use_state("")


    query=use_query
    async def load ():
        set_loading(True)

        try:
            r=await query.get(API_SUPERVISED)
            if r.ok:
                set_supervised(await r.json())
                

        except:
            
        


            pass
        set_loading(False)

    hooks.use_effect(lambda:load(),[])
    async def handle_action(sup_id,action,payload=None):
        endpoint=None
        if action=='approve':
            endpoint = f"/api/guardian/supervisions/{sup_id}/approve/"
            set_message(f"{action.capitalize()} completed successfully!")

        elif action=='release':
            endpoint = f"/api/guardian/supervisions/{sup_id}/release/"
        elif action=='extend':
             endpoint = f"/api/guardian/supervisions/{sup_id}/extend/"
        elif action=='view_package':
            from reactpy_django.hooks import use_websocket
            webs=await use_websocket
            await webs.exec(f'Window.location.href="/packages/{sup_id}/";')
            return
        else:
            set_message("Action failed: " + await r.text())

        if endpoint:
            r=await query.post(endpoint,json=payload or {})
            if r.ok:
                await load ()
            else:
                raise Exception(await r.text())
                
            
    container_style = {"padding": "22px", "fontFamily": "Inter, sans-serif", "color": "#dff6ff"}
    heading_style = {"fontSize": "28px", "fontWeight": "bold", "marginBottom": "10px", "textShadow": "0 0 10px #00eaff"}
    neon_section = html.div(
        {"style": {"padding": "16px", "background": "#0DCC56", "color": "#fff"}},
        TerminalHeader("GUARDIAN PANEL — Neon Terminal", "Approve supervised packages · manage unlock rules"),
        html.div(
            {"style": {"display": "grid", "gridTemplateColumns": "repeat(2,1fr)", "gap": "12px", "marginTop": "12px"}},
            NeonCard([
                html.h3("Supervised Packages"),
                html.ul({"style": {"listStyle": "none", "padding": 0}},
                    *[
                        html.li(
                            {"style": {"padding": "8px 6px", "borderBottom": "1px dashed rgba(255,255,255,0.03)"}},
                            html.strong(s.get("pack_name") or f"#{s.get('pck_id')}"),
                            html.div({"style": {"color": "#9aa1b2", "fontSize": "12px"}}, f"Status: {s.get('guardian_status')}"),
                            NeonButton("Review", on_click=lambda e, p=s: review_package(p))
                        )
                        for s in supervised
                    ]
                )
            ]),
            NeonCard([
                html.h3("Pending Approvals"),
                html.p("No pending approvals." if not supervised else "")
            ])
        )
    )

    supervision_section = html.div(
        {"style": container_style},
        html.h2({"style": heading_style}, "Guardian Supervision Panel"),
        GuardianToolBar(on_refresh=load),
        html.p({"style": {"opacity": 0.7}}, message),
        html.div("Loading…" if loading else ""),
        html.div(
            {"style": neon_section},
            *[SupervisionCard(s, on_action=handle_action) for s in supervised]
        )
    )

    return html.div({}, neon_section, supervision_section)

 
async def review_package(p):
    from reactpy_django.hooks import use_websocket
    webs=await use_websocket
    await webs.exec(f"window.location.href = '/supervised/{p.get('pck_id')}/';")
