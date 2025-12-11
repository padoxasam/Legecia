from reactpy import component,html,hooks
from frontend.components.neon import TerminalHeader,NeonButton,NeonCard,Metric
from reactpy_django.hooks import use_query
API_ASSIGNED='/api/package/assigned/'
API_UPLOAD='/milestone/upload/'
@component
def BeneficiaryDashboardPage():
    style= {"padding": "16px",
        "background": "#950CB1",
        "color": "#fff",
        "fontFamily": "sans-serif"}
    assigned,set_assigned=hooks.use_state([])
    query = use_query()
    async def load():
        try:
            r=await query.get(API_ASSIGNED)
            if r.ok:
                set_assigned(await r.json())
        except:
            pass
    hooks.use_effect(lambda:load(),[])
    return html.div({"style": style},
        TerminalHeader("BENEFICIARY PANEL — Neon Terminal", "View assigned packages · upload milestones"),
        html.div({"style":{"display":"flex", "gap":"12px", "marginTop":"12px"}},
                 NeonCard([html.h3("Assigned Packages"), html.ul({"style":{"listStyle":"none","padding":0}},
                     *[html.li({"style":{"padding":"8px 6px","borderBottom":"1px dashed rgba(255,255,255,0.03)"}},
                               html.strong(p.get("pack_name") or f"#{p.get('pack_id')}"),
                               html.div({"style":{"color":"#9aa1b2","fontSize":"12px"}}, p.get("pack_status", ""))) for p in assigned]
                     )]),
                 NeonCard([html.h3("Upload Milestone"),
                           html.p("Upload photos or PDF to match your user’s template"),
                           NeonButton("Upload Now", on_click=lambda e: redirect("/milestone/upload/"))
                           ])
        )
    )
async def redirect(url):
    from reactpy_django.hooks import use_websocket
    webs= await use_websocket
    await webs.exec(f"Window.location.href='{url}':")
