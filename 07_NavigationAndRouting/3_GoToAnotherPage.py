'''
In this section, we will learn how to go to the new page in Flet App.
'''

import flet as ft

def main(page: ft.Page):

    page.add(ft.Text(f"Initial Route: {page.route}"))

    def route_change(route):
        page.add(ft.Text(f"New Route: {page.route}"))
    
    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))

ft.app(target=main, view=ft.WEB_BROWSER)