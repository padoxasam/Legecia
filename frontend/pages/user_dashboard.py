from reactpy import component,html,hooks
from frontend.components.neon import TerminalHeader,NeonButton,NeonCard,Metric
from reactpy_django.hooks import use_query
API_PACKAGES='/api/package/'
API_ACTIVITY='/api/logs/my-activity/'


@component
def UserDashboardPage():
    style={
        "padding": "16px",
        "background": "#271414",
        "color": "#fff",
        "fontFamily": "sans-serif"}
    metrics, set_metrics = hooks.use_state({"packages": "...", "storage": "..." })
    recent, set_recent = hooks.use_state([])
    query = use_query()
    async def load():
        try:
            r1=await query.get(API_PACKAGES)
            if r1.ok:
                packs=await r1.json()
                set_metrics({'packages':str(len(packs)),'storage': '-'})
            r2=await use_query.get(API_ACTIVITY)
            if r2.ok:
                set_recent(await r2.json())
        except Exception:
            pass
    hooks.use_effect(lambda:load(),[])
    return html.div({"style": style},
        TerminalHeader("USER PANEL — Neon Terminal", "Upload packages · manage access · audit trail"),
        html.div({"style": {"display":"flex", "gap":"18px", "marginTop":"16px", "alignItems":"flex-start"}},
            html.div({"style":{"flex":"1", "display":"grid", "gridTemplateColumns":"repeat(3,1fr)", "gap":"12px"}},
                Metric("Packages", metrics["packages"], "Total packages uploaded"),
                Metric("Storage", metrics["storage"], "Used storage (approx)"),
                Metric("Unlocked", "0", "Packages unlocked for beneficiaries")
            ),
            html.div({"style":{"width":"420px"}}, 
                NeonCard([
                    html.h4("Quick Actions"),
                    html.div({"style":{"display":"flex","gap":"8px","marginTop":"8px"}},
                             NeonButton("Create Package", on_click=lambda e: window_location("/packages/create")),
                             NeonButton("Upload Files", on_click=lambda e: window_location("/milestone/create"))
                    )
                ])
            ))),html.div({"style":{"marginTop":"18px", "display":"grid", "gridTemplateColumns":"2fr 1fr", "gap":"12px"}},
            NeonCard([
                html.h3("Recent Activity"),
                html.ul({"style":{"listStyle":"none","padding":0,"margin":0}},
                        *[html.li({"style":{"padding":"8px 6px","borderBottom":"1px dashed rgba(255,255,255,0.03)"}}, 
                                 html.small(item.get("log_action") + " — " + item.get("log_at", ""))) for item in recent]
                )
            ]),
            NeonCard([
                html.h3("Status"),
                html.p("Terminal mode: Live monitoring enabled"),
                html.small({"style":{"color":"#9aa1b2"}}, "Connections: 3 | Guardian alerts: 0")
            ])
        )
async def window_location(url):
    from reactpy_django.hooks import use_websocket
    webs= await use_websocket
    await webs.exec(f"Window.location.href='{url}':")


