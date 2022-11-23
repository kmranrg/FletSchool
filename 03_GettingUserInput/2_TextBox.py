'''
In this section, we will learn about the functionality of Flet Textbox.
So, let's build a simple app which can say hello to a person.
'''

import flet as ft

def main(page: ft.Page):
    page.title = "Say Hello!"
    page.horizontal_alignment = "center"
    page.padding = 100

    user_name = ft.TextField(label="Enter name", width=300)
    print_name_column = ft.Column()

    def call_hello(e):
        if not user_name.value:
            user_name.error_text = "You forgot to enter the name!"
            page.update()
        else:
            page.clean()
            print_name_column.controls.append(ft.Text(f"Hello, {user_name.value}!"))
            page.add(print_name_column)

    page.add(
        user_name,
        ft.ElevatedButton("Say Hello!", on_click=call_hello),
        print_name_column
    )

ft.app(target=main)