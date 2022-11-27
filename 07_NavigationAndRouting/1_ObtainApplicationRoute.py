'''
In this section, we will obtaing the application route path in Flet.
'''

import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial Route: {page.route}"))

ft.app(target=main, view=ft.WEB_BROWSER)

'''
NOTE:

1) Grab the application URL (i.e. localhost URL)
2) Paste it in the web browser
3) At the end of the link, after `#` put `/test` and hit enter
4) You will see that the Initial Route path has been changed
'''