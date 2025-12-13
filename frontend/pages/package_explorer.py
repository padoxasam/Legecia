from reactpy import component,html,hooks
from reactpy_django.hooks import use_query
from frontend.components.layout import Layout
from frontend.components.package_public_card import PublicPackageCard
from frontend.components.neon import TerminalHeader

API_EXPLORE_URL='http://127.0.0.1:8000/api/explorer/'
@component
def PackageExplorerPage():
    
    search,set_search=hooks.use_state('')
    results,set_results=hooks.use_state([])
    query=use_query()
    async def fetch():
        try:
            res=await query.get(API_EXPLORE_URL)
            if res.ok:
                set_results(await res.json())
        except:
            pass
    
    hooks.use_effect(lambda:fetch(),[])
    
    
    filtered=[row for row in results
              if search.lower() in row['packa_name'].lower()
              or search.lower() in row['family_nickname'].lower()]
    return Layout(
            TerminalHeader("PACKAGE EXPLORER", "Search · Filter · Explore Available Packages"),

        html.div(
            {"style": {"padding": "25px", "fontFamily": "Orbitron", "color": "#d7e5ff"}},
            html.h1({"style": {"color": "#00eaff"}}, "🌐 Package Explorer"),

            html.input(
                {
                    "type": "text",
                    "placeholder": "Search public packages...",
                    "value": search,
                    "onChange": lambda e: set_search(e["target"]["value"]),
                    "style": {
                        "padding": "10px",
                        "width": "100%",
                        "marginTop": "20px",
                        "border": "1px solid #00eaff",
                        "background": "#06101f",
                        "color": "#fff",
                    },
                }
            ),html.div(
                {
                    "style": {
                        "marginTop": "25px",
                        "display": "grid",
                        "gridTemplateColumns": "repeat(auto-fill, minmax(300px, 1fr))",
                        "gap": "20px",
                    }
                },
                *[PublicPackageCard(pkg) for pkg in filtered],)))
