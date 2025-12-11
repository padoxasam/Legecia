from reactpy import component,html
@component
def AccessLogRow(log):
    color="#3acf3a" if log.get('Successfil_log') else "#e91919"
    return html.tr(
        {"style": {"borderBottom": "1px solid #033"}},
        html.td({"style": {"padding": "10px"}}, log.get("ip_address")),
        html.td({"style": {"padding": "10px"}}, log.get("device_info")),
        html.td({"style": {"padding": "10px"}}, log.get("login_start")),
        html.td({"style": {"padding": "10px"}}, log.get("logout") or "—"),
        html.td({"style": {"padding": "10px", "color": color}}, 
                "✓ Success" if log.get("successful_log") else "✗ Failed"),
        html.td({"style": {"padding": "10px"}}, log.get("failure_message") or "—"),)