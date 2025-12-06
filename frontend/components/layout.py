from reactpy import component, html
from .navbar import Navbar
from .sidebar import Sidebar
from .footer import Footer

@component
def Layout(content):
    return html.div( {'style':{'display':'flex',
                               'flexDirection':'row',
                               'width':'100%',
                               'minHeight':'100vh',
                               'backgroundcolor':'8b008b',}

    }, Sidebar(),html.div({ 'style': {'flex':'1',
                                     'padding':'25px',
                                     'display':'flex',
                                     'flexDirection':'column',
                                     'minHeight':'100vh',}
 },
 Navbar(),
 html.div({'style':{'marginTop':'20px'}},content),
 Footer(),
    )

    
    
    
    
    
    
    )