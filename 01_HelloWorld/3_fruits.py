'''
In this section, we will print list of fruits in one row.
'''

import flet as ft
from time import sleep

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("LIST OF FRUITS:\n")
        ]),
        ft.Row(controls=[
            ft.Text("Apple"),
            ft.Text("Banana"),
            ft.Text('Mango')
        ])
    )

ft.app(target=main)