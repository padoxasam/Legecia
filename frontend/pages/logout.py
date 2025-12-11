from reactpy import component,html,hooks
from reactpy_django.hooks import use_websocket
@component
def LogoutPage():
    message,set_message=hooks.use_state('Logging you out ....')
    async def perform_logout():
        webs=await use_websocket
        await webs.exec("""
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            localStorage.removeItem("username"); """)
        await webs.exec('window.location.href = "/login/";')
        set_message('Redirecting .....')
        hooks.use_effect(lambda:perform_logout(),[])
        return html.div(
        {
            "style": {
                "height": "100vh",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "background": "#00010F",
                "color": "#00FFFF",
                "fontFamily": "Orbitron",
                "fontSize": "22px",
                "textShadow": "0 0 12px #00FFFF",
            }
        },
        html.div(
            {"style": {"animation": "pulse 1.2s infinite"}},
            f'Logging out… {message}'))