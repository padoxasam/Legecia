from reactpy import component,html
@component
def Sidebar():
    links=[('Home','/'),
           ('Packages','/packages'),
           ('Milestone','/milestone'),
           ('Notifications','/notifications'),
           ('Switch Role', '/switch-role'),]
    return html.div({'style':{'width':'200px',
                              'backgroundcolor':'#d4a90f',
                              'color':'#b3f5de',
                              'padding':'20px',
                              'minheight':'120vh',}

    },html.h3({'style':{'marginBottom':'20px'}},'Navigation'),
    *[html.a({'href':url,'style':{'display':'block','margin':'15px','color':'white'}},name)
        for name,url in links],)