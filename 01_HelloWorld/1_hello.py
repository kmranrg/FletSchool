'''
In this section, we will learn to create a simple Hello World program in Flet framework.
'''

# importing the library
import flet as ft

# defining main function
def main(page: ft.Page):
    text = ft.Text(value="Hello, Anurag!", color="red")
    page.controls.append(text)
    page.update()

# starting the app
ft.app(target=main)

# for running it in web browser
'''
ft.app(target=main, view=ft.WEB_BROWSER)
'''

'''
Note: 

(i) When running Flet app in the browser a new user session is started for every opened tab or page.
(ii) When running as a desktop app there is only one session created.
'''