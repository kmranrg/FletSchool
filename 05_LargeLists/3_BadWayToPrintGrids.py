'''
In this section, we will print a grid (using `ft.Row(wrap=True)` and 
`ft.Column(wrap=True)`) with 5000 items, and we will it's disadvantages.
'''

import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    r = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(r)

    for i in range(5000):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(5, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)

'''
NOTE:

1) We can notice that it's very laggy (especially in web browser).
2) At the start of the program we are setting the value of 
    FLET_WS_MAX_MESSAGE_SIZE environment variable to 8000000 - this is the 
    maximum size of WebSocket message in bytes that can be received by Flet Server 
    rendering the page. Default size is 1 MB, but the size of JSON message 
    describing 5,000 container controls would exceed 1 MB, so we are increasing 
    allowed size to 8 MB.
'''