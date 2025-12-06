from reactpy import component,html,hooks
from reactpy_django.hooks import use_query
API_LOGIN_URL='http://127.0.0.1:8000/api/auth/login/'
@component
def LoginPage():
    username,set_username=hooks.use_state('')
    password,set_password=hooks.use_state('')
    message,set_message=hooks.use_state('')
    loading,set_loading=hooks.use_state(False)
    async def save_to_local_storage(access,refresh,username):
        from reactpy_django.hooks import use_websocket
        websocket=await use_websocket
        await websocket.exec(f"""
            localStorage.setItem("access_token", "{access}");
            localStorage.setItem("refresh_token", "{refresh}");
            localStorage.setItem("username", "{username}");
            """)
    async def redirect_to_home():
        from reactpy_django.hooks import use_websocket
        ws = await use_websocket()
        await ws.exec("window.location.href = '/';")
    def handle_login(event):
        event.prevent_default()
        async def send_request():
            set_loading(True)
            set_message('')

            response=await use_query.post(API_LOGIN_URL,json={'username':username,'password':password})
            set_loading(False)
            if response.ok:
                data=await response.json()
                await save_to_local_storage(data["access_token"],
                    data["refresh_token"],
                    data["user"]["username"],)
                
                set_message('Login Successful !')
                await redirect_to_home()
            else:
                set_message('Invalid Credentials !')
        return send_request
    return html.div( {'style':{"maxWidth": "400px",
                "margin": "50px auto",
                "padding": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "10px",
                "backgroundColor": "#51ade2",}}
                ,html.h3('Login'),
        html.form({'onSubmit':handle_login},
                  html.label('Username'),
                  html.input({'type':'text','value':username,'onChange':lambda e:set_username(e['target']['value']),
                                        }),
                html.br(),
                html.label('Password'),
                html.input({"type": "password",
                    "value": password,
                    "onChange": lambda e: set_password(e["target"]["value"]),}),
           html.br(),
           html.button({'type':'submit','style':{'marginTop':'20px',
                                                  "padding": "10px",
                        "backgroundColor": "#222",
                        "color": "white",
                        "borderRadius": "5px",
                        "cursor": "pointer",},},
            'Login'
               
           ),     

        ),
            html.p({'style':{'marginTop':"20px", 'color':'##6c5898'}},message),
    )