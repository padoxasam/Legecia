from reactpy import component,html,hooks
from frontend.components.layout import Layout
from frontend.components.milestone_helper import validate_file_role,filepreview
 
@component
def UploadMilestonePage(): # optimize ya 7g 
    templates,set_templates=hooks.use_state([
        {"id": 1, "name": "Birth Certificate"},
        {"id": 2, "name": "University Diploma"}],)
    selected_template,set_selected_template=hooks.use_state(None)
    file_list, set_file_list = hooks.use_state([])
    remarks, set_remarks = hooks.use_state("")
    errors, set_errors = hooks.use_state([])
    submitting, set_submitting = hooks.use_state(False)
    notice, set_notice = hooks.use_state("")
    def on_files_change(ev):
        files=ev['target']['files'] or []
        new_files=[]
        error=[]
        from collections import OrderedDict
        seen=OrderedDict()
        for f in files:
            ok,mssgt=validate_file_role(f['name'],'BENEFICIARY')
            if not ok:
                error.append(mssgt)
            else:
                if f['name'] not in seen:
                    seen[f['name']]=f
        if error:
            set_errors(error)
            return
        set_errors([])
        set_file_list(list(seen.values()))
    async def handle_submit(ev):
        ev.prevent_default()
        set_errors([])
        if not selected_template:
            set_errors(['Please Choose the Milestone template you are Uploading to ! '])
            return 
        if not file_list:
            set_errors(['Please Arrach at Least One File.'])
            return
        set_submitting(True)
        try:
            await __simulate_wait()
            set_notice('Milestone Has been Successfully Uploaded !')

            set_file_list([])
            set_remarks('')
            set_selected_template(None)
        except Exception as e :
            set_errors([str(e)])
        finally:
            set_submitting(False)
    def preview_block():
        if not file_list:
            return html.div({"style":{"color":"#777"}}, "No files selected.")
        return html.div({"style":{"display":"flex","gap":"12px","flexWrap":"wrap"}},
                        *[html.div({"style":{"width":"220px"}}, filepreview(f), html.div({"style":{"fontSize":"12px","marginTop":"6px"}}, f["name"])) for f in file_list])
    return Layout(
        html.div(
            {"style":{"maxWidth":"900px","margin":"18px auto","padding":"20px","borderRadius":"10px","background":"#fff"}},
            html.h2("Upload Milestone Proof (Beneficiary)"),
            html.form(
                {"onSubmit": handle_submit, "style":{"display":"grid","gap":"12px"}},
                html.div({}, html.label("Template"), 
                         html.select({"value": selected_template or "", "onChange": lambda e: set_selected_template(int(e["target"]["value"]) if e["target"]["value"] else None)},
                                     html.option({"value": ""}, "-- choose template --"),
                                     *[html.option({"value": t["id"]}, t["name"]) for t in templates]
                         )
                ),
                html.div({}, html.label("Files (images / pdfs / video allowed)"), html.input({"type":"file","accept":"*/*","onChange":on_files_change,"multiple":True})),
                html.div({}, preview_block()),
                html.div({}, html.label("Remarks (optional)"), html.textarea({"rows":4,"value":remarks,"onChange":lambda e:set_remarks(e["target"]["value"])})),
                html.div({}, html.button({"type":"submit","disabled":submitting}, "Upload Proof")),
                html.div({}, errors and html.ul({}, *[html.li({"style":{"color":"crimson"}}, e) for e in errors])),
                html.div({}, notice and html.div({"style":{"color":"green"}}, notice))
            )
        )
    )
async def __simulate_wait():
    import asyncio
    await asyncio.sleep(0.75)

