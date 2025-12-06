from reactpy import component,html,hooks
import requests
@component
def NotificationBadge():
    count,set_count=hooks.use_state(0)
    def fetch():
        try:
            r=requests.get('http://localhost:8000/api/notifications/unread-count')
            set_count(r.json().get('count',0))
        except:
            pass
    hooks.use_effect(fetch,[])
    return html.div({'style':{'backgroundcolor':"#e2e61a",'color':"#2b7ce7",'padding':'10px 20px',
                              'borderRadius':'25px','fontweight':'Bold'}},f'{count} 🔔')