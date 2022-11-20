'''
In this section, we will create a Simple Greetings App!
'''

import flet as ft

def main(page: ft.Page):
    page.title = "Greetings App"

    first_name = ft.TextField(label="First Name", autofocus=True)
    last_name = ft.TextField(label="Last Name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        first_name.focus()
        page.update()

    page.add(
        first_name, # just by looking this variable, we don't know whether it's a TextField or Text or ElevatedButton or which Flet control
        last_name, # just by looking this variable, we don't know whether it's a TextField or Text or ElevatedButton or which Flet control
        ft.ElevatedButton("Say Hello!", on_click=btn_click),
        greetings
    )

    '''
    NOTE:
    (i) As we have seen at top, in page.add(), by just using variable names, we are not able to decide it's Flet control type
    (ii) In order to sort out this problem, we can use `Ref`
    '''

ft.app(target=main)