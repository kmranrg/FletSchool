import flet as ft
from time import sleep

def main(page: ft.Page):
    page.title = "Timer App"
    page.horizontal_alignment = "center"
    page.padding = 40
    page.window_frameless = True
    page.window_height = 430
    page.window_width = 470

    seconds = ft.TextField(hint_text="seconds...", border_radius=30, width=120, text_align="center")

    def start_timer(e):
        sec_value = int(seconds.value)
        while sec_value:
            mins, secs = divmod(sec_value, 60)
            time.value = '{:02d} min {:02d} sec'.format(mins, secs)
            sleep(1)
            sec_value = sec_value - 1
            page.update()
        sleep(1)
        time.value = '{:02d} min {:02d} sec'.format(mins, sec_value)
        page.update()

    time = ft.Text(style="displayLarge")

    page.add(
        ft.Image(src=f"logo.png", height=90),
        ft.Container(padding = 20),
        ft.Row([seconds, ft.ElevatedButton("set timer", on_click=start_timer, color="green")], alignment="center"),
        ft.Container(padding = 20),
        time
    )

ft.app(target=main, assets_dir="assets")