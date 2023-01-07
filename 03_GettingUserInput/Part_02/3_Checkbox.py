'''
In this section, we will learn about the functionality
of Flet Checkbox control.

NOTE:
Flet provides a number of controls for building forms: 
TextField, Checkbox, Dropdown, ElevatedButton, etc.
'''

# let's build a simple to-do app
import flet as ft

def main(page: ft.Page):

    def checkbox_change(e):
        output_text.value = f"You have learned Swimming, that's great: {todo_check.value}"
        page.update()
    
    todo_check = ft.Checkbox(label="Learn Swimming", value=False, on_change=checkbox_change)
    output_text = ft.Text()

    page.add(
        todo_check,
        output_text
    )

ft.app(target=main)