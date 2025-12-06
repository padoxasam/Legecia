from reactpy import component, html , hooks
from reactpy_django.hooks import use_query
@component
def PackageForm(on_created=None):
    name,set_name=hooks.use_state('')
    description,set_description=hooks.use_state('')
    tags,set_tags=hooks.use_state('')
    pack_type,set_pack_type=hooks.use_state('')
    delivery,set_delivery=hooks.use_state('')
    has_expiry,set_has_expiry=hooks.use_state(False)
    expiry_at,set_expiry_at=hooks.use_state('')
    query=use_query()
    async def handle_submit(event):
        event.preventDefault()
        payload={'pack_name':name,
                 'description':description,
                'tags':tags,
                'pack_type':pack_type,
                'pack_delivery':delivery,
                'has_expiry': has_expiry,
                'expiry_at':expiry_at or None,}
        headers={'Content-Type':'application/json'}
        local=await query.local_storage()
        token=local.get('access_token')
        if token:
            headers['Authorization']= f'Bearer {token}'
        response= await query.post('/api/package',json=payload,headers=headers)
        if response.ok:
            data=await response.json()
            if on_created:
                on_created(data)
            set_name('')
            set_description('')
            set_tags('')
            set_pack_type('')
            set_delivery('')
            set_has_expiry(False)
            set_expiry_at('')
        else:
            print('Failed to Create Package',response.status,await response.text())

    return html.form(  {"onSubmit":handle_submit,
                      "style":{"background": "#FFFFFF",
                "padding": "18px",
                "borderRadius": "10px",
                "boxShadow": "0px 1px 4px rgba(0,0,0,0.08)",
                "marginBottom": "20px",
                "maxWidth": "500px",},},
                html.h4('Create Package'),
                html.label('Package Name'),
                html.input({'type':'text','value':name,'required':True,'onChange':lambda e:set_name(e['target']['value'])}),
                html.br(),
                html.label('Tags'),
                html.input({'value':tags,'onChange':lambda e:set_tags(e['target']['value'])}),
                html.br(),
                html.label('Delivery Method'),
                html.select({'value':delivery , 'onChange': lambda e:set_delivery(e['target']['value'])},
                html.option({'value':'Direct'},'Direct'),
                html.option({'value':'Guardian'},'Guardian'),
                html.option({'value':'Public'},'Public'),),
                html.br(),
                html.label({'style':{'marginTop':'15px'}},
                html.input({"type": "checkbox",
                "checked": has_expiry,
                "onChange": lambda e: set_has_expiry(e["target"]["checked"]),}),
                'Has Expiry ?',
                html.br(),
                html.label('Expiry Date'),
                html.input({'type':'Date','value':expiry_at, 'onChange': lambda e:set_expiry_at(e['target']['value'])}),
                html.br(),
                html.button({"type": "submit",
                "style": {
                    "marginTop": "15px",
                    "padding": "10px 16px",
                    "background": "#111827",
                    "color": "white",
                    "border": "none",
                    "borderRadius": "6px",
                    "cursor": "pointer",},},
                "Create Package",),))
    