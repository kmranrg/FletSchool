'''
In this section, we are creating a To-Do App.
'''

# importing the library
import flet as ft

# defining the main function
def main(page: ft.Page):

    # role of button
    def button_clicked(e):
        page.add(ft.Checkbox(label=input_text.value))

    # taking input from user
    input_text = ft.TextField(hint_text="What needs to be done...", width=300)

    # aligning the input text and button in a row
    page.add(ft.Row([
        input_text,
        ft.ElevatedButton(text="Add",on_click=button_clicked)
    ]))

# calling the app
ft.app(target=main)