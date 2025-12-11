from reactpy import component, html

@component
def PublicPackageCard(pkg):
    return html.div(
        {
            "style": {
                "padding": "20px",
                "borderRadius": "10px",
                "backgroundColor": "#0b1222",
                "border": "2px solid #00eaff",
                "boxShadow": "0 0 15px #00eaff",
                "color": "#fff",
                "fontFamily": "Orbitron",
            }
        },
        html.h3({"style": {"color": "#00eaff"}}, pkg.get("packa_name")),
        html.p({}, f"Family: {pkg.get('family_nickname')}"),
        html.p({}, f"Public: {'Yes' if pkg.get('is_public') else 'No'}"),
        html.p({}, f"Posted: {pkg.get('posted_at')}"),
    )
