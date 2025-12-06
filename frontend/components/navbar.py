from reactpy import component,html
from .notification_badge import NotificationBadge
 
@component
def Navbar():
    return html.div(
        {'style':{'height':'60px',
                  'backgroundcolor':'white',
                  'borderBottom':'1px solid #ddd',
                  'display':'flex',
                  'allignItems':'center',
                  'justifyContent':'space-between',
                  'padding':'0  25px',
                  'position':'sticky',
                  'top':'0',
                  'zindex':'1000'}
},
html.h2('LEGECIA Panel'),
NotificationBadge()







    )