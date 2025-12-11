from reactpy import component,html,hooks
from reactpy_django.hooks import use_query
from frontend.components.layout import Layout
API_GET_ROLES='http://127.0.0.1:8000/api/auth/my-roles/'
API_SET_ROLE='http://127.0.0.1:8000/api/auth/set-role/'

@component
def SwitchRolePage():
    roles,set_roles=hooks.use_State([])
    message,set_message=hooks.use_State('')
    loading,set_loading=hooks.use_state(False)

    query=use_query
    async def load_roles():
        res=await query.get(API_GET_ROLES)
        if res.ok:
            data=await res.json()
            set_roles(data.get('roles',[]))
    hooks.use_effect(lambda:load_roles(),[])
    async def switch_role(selected_role):
        set_loading(True)
        res=await use_query.post(API_SET_ROLE,json={'role':selected_role})
        set_loading(False)
        if res.ok:
            from reactpy_django.hooks import use_websocket
            webs=await use_websocket
            await webs.exec(f'localstorage.setItem("active_role","{selected_role}");')
            await webs.exec(f'window.location.href = "/dashboard/{selected_role.lower()}/";')
        else:
            set_message('Unable to switch Role !/Email Us ON') ############################### 
    def render_role_card(role):
        return html.div(
            {
                "style": {
                    "padding": "20px",
                    "border": "2px solid #00eaff",
                    "backgroundColor": "#07101d",
                    "boxShadow": "0 0 15px #00eaff",
                    "borderRadius": "12px",
                    "cursor": "pointer",
                    "textAlign": "center",
                    "transition": "0.3s",
                },
                "onClick": lambda e: switch_role(role),
            },
            html.h2(
                {"style": {"color": "#00eaff", "fontFamily": "Orbitron"}},
                f"🔹 {role}"
            ),
            html.p({"style": {"color": "#9acfff"}}, "Click to switch role"))
    return Layout(
        html.div(
            {"style": {"padding": "30px", "fontFamily": "Orbitron", "color": "#d7e5ff"}},
            html.h1({"style": {"color": "#00eaff"}}, "🔄 Switch Role"),

            html.div(
                {
                    "style": {
                        "marginTop": "30px",
                        "display": "grid",
                        "gridTemplateColumns": "repeat(auto-fill, minmax(250px, 1fr))",
                        "gap": "30px",
                    }
                },
                *[render_role_card(role) for role in roles],
            ),

            html.p({"style": {"marginTop": "20px", "color": "#ff4444"}}, message),
        )
    )
