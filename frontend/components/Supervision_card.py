from reactpy import component , html , hooks
from reactpy_django.hooks import use_query

@component
def SupervisionCard(supervision,on_action=None):
    busy,set_busy=hooks.use_state(False)
    message,set_message=hooks.use_state('')
    async def do_action(action,payload=None):
        set_busy(True)
        try:
            if on_action:
                await on_action(supervision['id'],action,payload)
            set_message(f'{action} Successfully Executed !')
        except Exception as e :
            set_message(f'{action} Failed ❌:(getattr(e,"message",str(e)))' )
        finally:
            set_busy(False)
    status_badge = html.span({"style": {"padding": "6px 10px","borderRadius": "999px","fontWeight": "600","fontSize": "12px","backdropFilter": "blur(6px)","background": "#ffffff20","color": "#ffffff","boxShadow": "inset 0 -2px 8px rgba(255,255,255,0.03)"}}, supervision.get("guardian_status", "Unknown"))
    return html.div({"style": {"padding": "18px","borderRadius": "14px","background": "linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03))","border": "1px solid rgba(255,255,255,0.06)","boxShadow": "0 8px 30px rgba(8,12,20,0.5)","color": "#f6fbff","minWidth": "320px"}}, html.div({"style": {"display": "flex","justifyContent": "space-between","alignItems": "center"}}, html.div({}, html.h3({"style": {"margin": 0,"fontFamily": "Inter, system-ui","fontWeight": 700}}, supervision.get("pack_name", "—")), html.small({"style": {"opacity": 0.8}}, f"Package ID: {supervision.get('pack_id')}")), status_badge), html.div({"style": {"marginTop": "12px","display": "grid","gridTemplateColumns": "1fr 1fr","gap": "8px"}}, html.div({}, html.p({"style": {"margin": 0,"fontSize": "14px","opacity": 0.9}}, f"Owner: {supervision.get('user', {}).get('full_name') or supervision.get('user', {}).get('username')}"), html.p({"style": {"margin": 0,"fontSize": "13px","opacity": 0.75}}, f"Beneficiary: {supervision.get('beneficiary', {}).get('full_name') or supervision.get('beneficiary', {}).get('username')}")), html.div({}, html.p({"style": {"margin": 0,"fontSize": "13px","opacity": 0.8}}, f"Created: {supervision.get('created_at', '—')}"), html.p({"style": {"margin": 0,"fontSize": "13px","opacity": 0.8}}, f"Expiry: {supervision.get('expiry_at', '—')}"))), html.div({"style": {"marginTop": "12px","display": "flex","gap": "8px","alignItems": "center"}}, html.button({"onClick": lambda e: do_action("view_package"),"style": {"padding": "8px 12px","borderRadius": "10px","border": "none","cursor": "pointer","background": "rgba(255,255,255,0.06)","color": "#dff6ff"}}, "View Package"), html.button({"onClick": lambda e: do_action("approve"),"style": {"padding": "8px 12px","borderRadius": "10px","border": "none","cursor": "pointer","background": "#00c48c","color": "#041014","fontWeight": 700}}, "Grant Access"), html.button({"onClick": lambda e: do_action("extend"),"style": {"padding": "8px 12px","borderRadius": "10px","border": "none","cursor": "pointer","background": "#ffb86b","color": "#041014","fontWeight": 700}}, "Extend"), html.button({"onClick": lambda e: do_action("release"),"style": {"padding": "8px 12px","borderRadius": "10px","border": "none","cursor": "pointer","background": "#ff6b6b","color": "#041014","fontWeight": 700}}, "Release")), html.div({"style": {"marginTop": "10px","minHeight": "18px"}}, html.small(message)))
