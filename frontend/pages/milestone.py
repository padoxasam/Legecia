from reactpy import component, html
from frontend.components.layout import Layout

@component
def MilestonesPage():
    return Layout(
        html.div(
            {
                "style": {
                    "padding": "25px",
                    "color": "#e0e8ff",
                    "fontFamily": "Arial",
                    "animation": "fadeIn 0.6s"
                }
            },
            html.h1(
                {"style": {"color": "#00f2ff", "textShadow": "0 0 10px #00f2ff"}},
                "Milestone Center"
            ),

            html.p(
                {"style": {"opacity": "0.8", "marginBottom": "25px"}},
                "Manage, upload, and verify milestones in one place."
            ),

            html.div(
                {
                    "style": {
                        "display": "flex",
                        "gap": "20px",
                        "flexWrap": "wrap"
                    }
                },

                card("Create Milestone", "/milestones/create", "#00e6f6"),
                card("Upload Milestone", "/milestones/upload", "#a800ff"),
                card("Preview Milestones", "/milestones/preview", "#ff0099"),),))
def card(title, link, glow):
    return html.a({
            "href": link,
            "style": {
                "width": "250px",
                "padding": "20px",
                "borderRadius": "12px",
                "backgroundColor": "rgba(255,255,255,0.06)",
                "textDecoration": "none",
                "color": "white",
                "boxShadow": f"0 0 12px {glow}",
                "transition": "0.3s",}},
        html.h3(
            {"style": {"marginBottom": "10px"}},
            title),
        html.p(
            {"style": {"fontSize": "14px", "opacity": "0.8"}},
            "Click to open"))
