import flet as ft

'''
Theory: Why do we need User Controls

1) UserControl allows building isolated re-usable components
    by combining existing Flet Controls.

2) UserControl must implement build() that is called 
    to build the control's UI.

3) build() function should return a single Control 
    instance of a List of controls.
'''

class GreeterControl(ft.UserControl):
    def build(self):
        return ft.Row([ft.Text("Hello World!"), ft.ElevatedButton("I am a button")], alignment="center")

def main(page: ft.Page):
    page.add(GreeterControl())

ft.app(target=main)