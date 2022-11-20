'''
In this section, we will create a Simple Greetings App with Ref
'''

import flet as ft

def main(page: ft.Page):

    page.title = "Greetings App"

    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        # whenever we want to access the Referenced Control (Ref) variable, we just need to use `Ref.current` property
        greetings.current.controls.append(ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
        first_name.current.value = ""
        last_name.current.value = ""
        first_name.current.focus()
        page.update()

    page.add(
        ft.TextField(ref=first_name, label="First Name", autofocus=True),
        ft.TextField(ref=last_name, label="Last Name"),
        ft.ElevatedButton("Say Hello!", on_click=btn_click),
        ft.Column(ref=greetings) # all the Flet controls have `ref` property
    )

ft.app(target=main)

'''
NOTE:

1) Now we can clearly see in `page.add()` the structure of the page and all the controls it's built of.
2) Yes, the logic becomes a little bit more verbose as you need to add .current. to access ref's control,
   but it's a matter of personal preference :)
'''