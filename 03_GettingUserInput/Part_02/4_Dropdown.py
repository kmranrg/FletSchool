'''
In this section, we will learn about Flet Dropdown Control.
'''

import flet as ft

def main(page: ft.Page):

    page.title = "Color Drodown"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def btn_click(e):
        print_output.value = f"You have selected => {color_dropdown.value}"
        page.update()

    color_dropdown = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue")
        ]
    )

    button = ft.ElevatedButton(text="Submit", on_click=btn_click)
    print_output = ft.Text()

    page.add(
        color_dropdown,
        button,
        print_output
    )

ft.app(target=main)

'''
NOTE:

If you don't select anything from Dropdown and click on Submit button,
it will print None.
'''