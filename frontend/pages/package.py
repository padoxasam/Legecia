from reactpy import component, html, hooks
from reactpy_django.hooks import use_query
from frontend.components.package_card import PackageCard
from frontend.components.package_form import PackageForm
@component
def PackagePage():
    query=use_query()
    packages,set_packages=hooks.use_state([])
    loading,set_loading=hooks.use_state(True)
    search,set_search=hooks.use_state('')
    filter_delivery, set_filter_delivery =hooks.use_state('')
    filter_type,set_filter_type=hooks.use_state('')
    async def load_packages():
        set_loading(True)
        parameters={}
        if search:
            parameters['q']=search
        if filter_delivery:
            parameters['delivery']=filter_delivery
        if filter_type:
            parameters['pack_type']=filter_type
        query_string='' 
        if parameters:
            query_string= '?' + '&'.join(f'{k}={parameters[k]}' for k in parameters)
        response=await query.get(f'/api/package/{query_string}')
        if response.ok:
            set_packages(await response.json())
        else:
            set_packages([])
        set_loading(False)
    hooks.use_effect(lambda:load_packages(),[])
    def refresh_after_create(new_pkg):
        set_packages([new_pkg]+packages)
    return html.div({'style':{'padding':'25px'}},
                    html.h3('Packages'),
    html.div(
            {"style": {"display": "flex", "gap": "12px", "marginBottom": "18px"}},
            html.input({
                "placeholder": "Search...",
                "value": search,
                "onChange": lambda e: set_search(e["target"]["value"]),
            }),
            html.select(
                {"value": filter_delivery, "onChange": lambda e: set_filter_delivery(e["target"]["value"])},
                html.option({"value": ""}, "All Delivery Modes"),
                html.option({"value": "Direct"}, "Direct"),
                html.option({"value": "Guardian"}, "Guardian"),
                html.option({"value": "public"}, "Public"),
            ),
            html.select(
                {"value": filter_type, "onChange": lambda e: set_filter_type(e["target"]["value"])},
                html.option({"value": ""}, "All Types"),
                html.option({"value": "Event-Based"}, "Event-Based"),
                html.option({"value": "Location-Based"}, "Location-Based"),
                html.option({"value": "Countdown"}, "Countdown"),
            ),
            html.button({"onClick": lambda _ : load_packages()}, "Apply Filters"),
        ),
PackageForm(on_created=refresh_after_create),
html.br(),
html.div(
            {"style": {"marginTop": "20px"}},
            (
                html.p("Loading packages...") if loading else
                html.p("No packages found.") if not packages else
                html.div(*[PackageCard(p) for p in packages])
            ),
        ),
    )