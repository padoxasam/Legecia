from reactpy import component,html
from frontend.components.layout import Layout
@component
def HomePage():
    return Layout(html.div({'style':{'padding':'25px'}},html.h1('Welcome To Legecia'))

)