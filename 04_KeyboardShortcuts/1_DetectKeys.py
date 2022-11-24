'''
In this section, we will detect the Keyboard Events in Flet.
'''

#NOTE:
'''
To capture all keystrokes, we need to implement `page.on_keyboard_event` handler.
Event handler parameter `e` is an instance of `KeyboardEvent` class having the following properties:

(i) key - a textual representation of a pressed key, Example: A, Enter, F5, etc.
(ii) shift - `True` if "Shift" key is pressed.
(iii) ctrl - `True` if "Control" key is pressed.
(iv) alt - `True` if "Alt or Option" key is pressed.
(v) meta - `True` if "Command" key is pressed.
'''

# let's build a simple app which can detect the keyboard strokes

import flet as ft
    
def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboard # now this on_keyboard() is going to call automatically whenever user presses any key or any key combination

    page.add(
        ft.Text("Press any key (or any key combination)...")
    )

ft.app(target=main)