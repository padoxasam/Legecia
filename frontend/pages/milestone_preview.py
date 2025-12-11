from reactpy import component, html, hooks
from frontend.components.layout import Layout
from frontend.components.milestone_helper import FilePreview

@component
def MilestoneDetailsPage(milestone_id:int= None):
    loading, set_loading = hooks.use_state(True)
    data, set_data = hooks.use_state(None)
    action_msg, set_action_msg = hooks.use_state("")
    async def load():
        set_loading(True)
        await __simulate_wait()
        set_data({"id": milestone_id or 1,
            "template_name": "Birth Certificate",
            "family": "Johnson",
            "created_by": "user123",
            "reference_files": [{"name": "template_ref.pdf", "url": "/static/demo/ref.pdf"}],
            "uploads": [
                {"id": 101, "by": "bene_ahmed", "status": "Pending", "file": {"name": "photo.jpg", "url": "/static/demo/photo.jpg"}, "remarks": "Scanned image"},
                {"id": 102, "by": "bene_mina", "status": "Verified", "file": {"name": "scan.pdf", "url": "/static/demo/scan.pdf"}, "remarks": "Official scan"}
            ],
            "notes": "Template created to collect official birth documents."
        })
        set_loading(False)
    hooks.use_effect(lambda:load(),[])
    def verify_upload(upload_id):
        set_action_msg(f'Verified Upload #{upload_id}(backend hook pending)')
    def reject_upload(upload_id):
        set_action_msg(f'Rejected Upload #{upload_id}(backend hook pending)')
    if loading:
        return Layout(html.div({"style":{"padding":"24px"}}, html.h3("Loading milestone...")))
    ref_files=data['reference_files']
    uploads=data['uploads']
    return Layout(
        html.div(
            {"style":{"maxWidth":"980px","margin":"20px auto","padding":"18px","background":"#fff","borderRadius":"10px"}},
            html.h2(f"Milestone — {data['template_name']}"),
            html.div({"style":{"color":"#666"}}, f"Family: {data['family']} — Created by: {data['created_by']}"),
            html.hr(),
            html.h3("Reference Documents"),
            html.div({"style":{"display":"flex","gap":"12px"}}, *[FilePreview(f) for f in ref_files]),
            html.hr(),
            html.h3("Beneficiary Uploads"),
            html.div(
                {"style":{"display":"grid","gap":"12px"}},*[html.div( {"style":{"display":"flex","justifyContent":"space-between","alignItems":"center","padding":"12px","border":"1px solid #eee","borderRadius":"8px"}},
                        html.div(
                            {},
                            html.div({"style":{"fontWeight":"700"}}, f"{u['by']} — #{u['id']}"),
                            html.div({"style":{"color":"#333"}}, u['remarks']),
                        ),
                        html.div(
                            {"style":{"display":"flex","gap":"8px","alignItems":"center"}},
                            FilePreview(u["file"]),
                            html.div(
                                {},
                                html.button({"onClick": lambda _u=u: verify_upload(_u["id"]), "style":{"marginRight":"8px"}}, "Verify"),
                            html.button({"onClick": lambda _u=u: reject_upload(_u["id"])}, "Reject")
                            )
                        )
                    ) for u in uploads
                ]
            ),
            action_msg and html.div({"style":{"marginTop":"12px","color":"green"}}, action_msg)
        )
    )
async def __simulate_wait():
    import asyncio
    await asyncio.sleep(0.75)