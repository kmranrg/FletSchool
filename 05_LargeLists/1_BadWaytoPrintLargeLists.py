'''
Problem with `Row` and `Column` Controls:

We can use `Row` and `Column` to display list in most of the cases but 
when it comes to print hundreds of thousands of items then `Row` and `Column`
are ineffective with lagging UI.
'''

# let's print 500 text messages using Flet `Text` control

import flet as ft

def main(page: ft.Page):
    for i in range(5000):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)

"""
NOTE:

The above method is very ineffective, as the scrolling becomes really slow (especially in web browser).
So, for printing large no of times, we should use `ListView` (or `GridView`) instead.
"""