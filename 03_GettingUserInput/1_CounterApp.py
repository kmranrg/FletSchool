'''
In this section, we will understand the use of buttons with the
help of Counter App.
'''

import flet as ft

def main(page: ft.Page):
    page.title = "Counter App"
    page.vertical_alignment = "center"

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment="center"
        )
    )

ft.app(target=main)