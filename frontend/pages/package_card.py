from reactpy import component, html
@component

def PackageCard(package :dict):
    unlocked=package.get('unlcoked',False)
    unlocked_label=' Unlocked 🔓 ' if unlocked else 'Locked 🔒'
    
    return html.div( {'style':{"border": "1px solid #E5E7EB",
                "borderRadius": "10px",
                "padding": "16px",
                "backgroundColor": "#F3D9D9",
                "boxShadow": "0px 2px 5px rgba(0, 0, 0, 0.05)",
                "marginBottom": "14px",}
    },
    html.h2(package.get('Pack Name',f'Package #{package.get('pack_id')}')),
    html.div(
            {
                "style": {
                    "display": "flex",
                    "justifyContent": "space-between",
                    "fontSize": "14px",
                    "color": "#6B7280",
                }
            },
            html.span(f"Owner: {package.get('owner', 'Unknown')}"),
            html.span(f"{unlocked_label} • {package.get('pack_status', '--')}"),   ),
            html.div(
            {"style": {"marginTop": "10px"}},
            html.a(
                {
                    "href": f"/packages/{package.get('pack_id')}/",
                    "style": {
                        "padding": "6px 12px",
                        "border": "1px solid #3B82F6",
                        "borderRadius": "6px",
                        "color": "#3B82F6",
                        "textDecoration": "none",
                        "fontSize": "14px",
                    },
                },
                "View Details",
            ),
        ),     
    )