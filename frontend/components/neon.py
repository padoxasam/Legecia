from reactpy import component,html
palette={ "bg": "#05040a",
    "panel": "#0b0820",
    "accent": "#00f0ff",
    "accent_2": "#9c097c",
    "muted": "#1010d3",
    "glow": "0 0 18px rgba(0,240,255,0.15), 0 0 30px rgba(255,0,200,0.06)"}
@component
def TerminalHeader(title:str,subtitle:str=''):
    return html.div({
            "style": {
                "padding": "10px 16px",
                "borderBottom": f"1px solid rgba(255,255,255,0.04)",
                "boxShadow": palette["glow"],
                "display": "flex",
                "flexDirection": "column",
                "gap": "4px", } },html.div({"style": {"display": "flex", "alignItems": "center", "gap": "12px"}},
                 html.span({"style": {"width": "10px", "height": "10px",
                                      "borderRadius": "50%", "background": palette["accent"]}}),
                 html.h2({"style": {"margin": 0, "fontSize": "18px", "letterSpacing": "0.6px"}}, title)
                 ),
        html.small({"style": {"color": palette["muted"], "marginTop": "2px"}}, subtitle))
@component
def NeonCard(children,style=None):
    sty={ "background": palette["panel"],
        "borderRadius": "10px",
        "padding": "14px",
        "boxShadow": palette["glow"],
        "border": f"1px solid rgba(255,255,255,0.03)"}
    if style:
        sty.update(style)
    return html.div({'style':sty},children)
@component
def NeonButton(label:str,on_click=None,small=False):
    sty={ "padding": "8px 12px" if not small else "6px 10px",
        "borderRadius": "8px",
        "background": f"linear-gradient(90deg, {palette['accent']} 0%, {palette['accent_2']} 100%)",
        "border": "none",
        "cursor": "pointer",
        "fontWeight": "600"}
    return html.button({'style':s,'onClick':on_click},label)
@component
def Metric(title:str,value:str,hint:str=''):
    return NeonCard([
        html.div({"style": {"display": "flex", "justifyContent": "space-between", "alignItems": "baseline"}},
                 html.small({"style": {"color": palette["muted"]}}, title),
                 html.h3({"style": {"margin": 0}}, value)
                 ),
        html.small({"style": {"color": palette["muted"]}}, hint)
    ], style={"minWidth": "160px"})