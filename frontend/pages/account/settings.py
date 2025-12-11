from reactpy import component,html
from frontend.components.layout import Layout
from frontend.components.neon import NeonButton,NeonCard,TerminalHeader,Metric
@component
def AccountsettingsPage():
    return Layout(html.div(
            {
                "style": {
                    "padding": "25px",
                    "color": "#e2e8f0",
                    "fontFamily": "monospace",
                }
            },
            TerminalHeader("ACCOUNT SECURITY CENTER", "Manage your login & protection settings"),

            html.div(
                {
                    "style": {
                        "display": "grid",
                        "gridTemplateColumns": "repeat(2, 1fr)",
                        "gap": "20px",
                        "marginTop": "20px",
                    }
                },
                NeonCard([
                    html.h3("Change Email"),
                    html.p("Update your login email for account access."),
                    NeonButton("Manage Email", on_click=lambda e: goto("/account/settings/email")),
                ]),
                NeonCard([
                    html.h3("Change Password"),
                    html.p("Update your password — you will receive a security alert."),
                    NeonButton("Update Password", on_click=lambda e: goto("/account/settings/password")),
                ]),NeonCard([
                    html.h3("Two-Factor Authentication"),
                    html.p("Enable an extra layer of security."),
                    NeonButton("Manage 2FA", on_click=lambda e: goto("/account/settings/2fa")),
                ]),NeonCard([
                    html.h3("Security Log"),
                    html.p("View recent login attempts and suspicious activity."),
                    NeonButton("View Logs", on_click=lambda e: goto("/account/settings/security-log")),
                ]),
            )
        ))
async def goto(url):
    from reactpy_django.hooks import use_websocket
    webs=await use_websocket()
    await webs.exce(f'Window.location.href="{url}";')
    