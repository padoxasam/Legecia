from reactpy import component,html,hooks
from frontend.components.layout import Layout
from frontend.components.milestone_helper import exit_of,validate_file_role

@component
def CreateMilestonePage():
    name, set_name = hooks.use_state("")
    family, set_family = hooks.use_state("")
    description, set_description = hooks.use_state("")
    ref_file,set_ref_file = hooks.use_state(None)
    errors,set_errors = hooks.use_state([])
    saving,set_saving = hooks.use_state(False)
    message,set_message = hooks.use_state("")
    def on_file_change(ev):
        f=ev['target']['files'][0] if ev['target']['files'] else None
        if not f:
            set_ref_file(None)
            return
        ok,mssg=validate_file_role(f['name'],'USER')
        if not ok:
            set_errors([mssg])
            set_ref_file(None)
        else:
            set_errors([])
            set_ref_file(f)
    async def handle_submit(ev):
        ev.prevent_default()
        set_errors([])
        if not name.strip():
            set_errors('Template Name is Required !')
            return
        if not family.strip():
            set_errors({'Family name is Required !'})
            return
        if not ref_file:
            set_errors(['Please attach at least one reference Document !'])
            return
        set_saving(True)
        try:
            await __simulate_wait()
            set_message('Template Created Successfully !')
            set_name('')
            set_family('')
            set_description('')
            set_ref_file(None)
        except Exception as e:
            set_errors([str(e)])
        finally:
            set_saving(False)
        return Layout(
        html.div(
            {"style":{"maxWidth":"780px","margin":"20px auto","padding":"18px","background":"#fff","borderRadius":"10px"}},
            html.h2("Create Milestone Template"),
            html.form(
                {"onSubmit": handle_submit, "style":{"display":"grid","gap":"12px"}},
                html.div({}, html.label("Template name"), html.input({"type":"text","value":name,"onChange":lambda e:set_name(e["target"]["value"]),"required":True})),
                html.div({}, html.label("Family name"), html.input({"type":"text","value":family,"onChange":lambda e:set_family(e["target"]["value"]),"required":True})),
                html.div({}, html.label("Short description (optional)"), html.textarea({"value":description,"onChange":lambda e:set_description(e["target"]["value"]),"rows":4})),
                html.div({}, html.label("Reference document (user allowed formats)"), html.input({"type":"file","accept":"*/*","onChange":on_file_change})),
                html.div({}, 
                    html.button({"type":"submit","disabled":saving}, "Create Template"),
                    html.span({'style':{'marginLeft':'12px','color':'#666'}}, "You can upload multiple documents later when editing the template.")
                ),
                html.div({}, errors and html.ul({}, *[html.li({"style":{'color':'crimson'}}, e) for e in errors])),
                html.div({}, message and html.div({"style":{"color":"green"}}, message)))))
async def __simulate_wait():
    import asyncio
    await asyncio.sleep(0.75)    