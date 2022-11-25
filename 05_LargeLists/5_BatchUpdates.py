'''
Theory:

When page.update() is called a message is being sent to Flet server over WebSockets 
containing page updates since the last page.update(). Sending a large message with 
thousands of added controls could make a user waiting for a few seconds until the 
messages is fully received and controls rendered.

To increase usability of your program and present the results to a user as soon as 
possible you can send page updates in batches. For example, the following program adds 
5,100 child controls to a ListView in batches of 500 items
'''

import flet as ft

def main(page: ft.Page):

    # add ListView to a page first
    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(ft.Text(f"Line {i}"))
        # send page to a page
        if i % 500 == 0:
            page.update()
    # send the rest to a page
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)