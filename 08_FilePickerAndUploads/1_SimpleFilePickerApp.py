'''
Theory;

1) File picker Control opens a native OS dialog for selecting files and directories.
2) File picker allows opening three dialogs:
    (i) pick_files(): one or multiple, any files or only specific types
    (ii) save_file(): choose directory and file name
    (iii) get_directory_path(): select directory
3) When running Flet app in a browser only "Pick files" option is available and 
    it's used for uploads only as it, obviously, doesn't return a full path to a 
    selected file.
4) Where file picker really shines is a desktop! All three dialogs return full 
    paths to selected files and directories - great assistance to your users!
'''

# let's build a simple file picker app
import flet as ft

def main(page:ft.Page):

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.update()

    page.add(
        ft.ElevatedButton("Choose Files...", on_click=lambda _: file_picker.pick_files(allow_multiple=False))
    )

ft.app(target=main, view=ft.WEB_BROWSER)