'''
Theory:

When FilePicker Control dialog is closed `FilePicker.on_result` event handler is called which
event object has one of the following properties set:
    (i) `files` - "Pick files" dialog only, a list of selected files
                    or `None` if dialog was cancelled
    (ii) `path` - "Save file" and "Get directory" dialogs, a full path
                    to a file or directory or `None` if dialog was cancelled
'''

# in this section, we will print the path of the selected file from FilePicker Control

import flet as ft

def main(page:ft.Page):

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    page.update()

    page.add(
        ft.ElevatedButton("Choose Files...", on_click=lambda _: file_picker.pick_files(allow_multiple=True))
    )

ft.app(target=main, view=ft.WEB_BROWSER)