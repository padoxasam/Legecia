from reactpy import component,html,hooks 
@component
def GuardianToolBar(on_refresh=None):
    loading,set_loading=hooks.use_state(False)
    async def refresh():
        set_loading(True)
        try:
            if on_refresh():
                await on_refresh()
        finally:
            set_loading(False)
        return html.div(
        {"style": {
            "display": "flex",
            "gap": "12px",
            "alignItems": "center",
            "justifyContent": "space-between",
            "marginBottom": "18px"
        }},
        )