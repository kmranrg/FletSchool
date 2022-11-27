'''
Theory:

Every time the route in the URL is changed (by editing the URL 
or navigating browser history with Back/Forward buttons) Flet calls 
`page.on_route_change` event handler.
'''

# let's implement the above theory

import flet as ft

def main(page: ft.Page):

    page.add(ft.Text(f"Initial Route: {page.route}"))

    def route_change(route):
        page.add(ft.Text(f"New Route: {page.route}"))

    page.on_route_change = route_change

    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)