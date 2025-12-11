from reactpy import component, html, hooks

@component
def App():
    count, set_count = hooks.use_state(0)

    def increment(event):
        set_count(count + 1)

    return html.div(
        html.h1("Hello from ReactPy!"),
        html.p(f"Count: {count}"),
        html.button({"on_click": increment}, "Increment")
    )
