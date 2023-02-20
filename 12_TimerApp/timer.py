import flet as ft
from time import sleep

def main(page: ft.Page):
    page.title = "Timer App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"
    page.padding = 40
    page.window_frameless = True
    page.window_height = 490
    page.window_width = 490

    seconds = ft.TextField(hint_text="seconds...", border_radius=30, width=120, text_align="center")

    def start_timer(e):
        button.visible = False
        sec_value = int(eval(seconds.value))
        while sec_value:
            mins, secs = divmod(sec_value, 60)
            time.value = '{:02d} min {:02d} sec'.format(mins, secs)
            sleep(1)
            sec_value = sec_value - 1
            page.update()
        sleep(1)
        time.value = '{:02d} min {:02d} sec'.format(mins, sec_value)
        button.visible = True
        page.update()

    time = ft.Text(style="displayLarge", color="white")
    button = ft.ElevatedButton("set timer", on_click=start_timer, color="green")

    page.add(
        ft.Image(src=f"logo.png", height=90),
        ft.Container(padding = 20),
        ft.Row([seconds, button], alignment="center"),
        ft.Container(padding = 20),
        time,
        ft.Container(padding= 20),
        ft.Text("Designed and Developed by: kmranrg (Instagram)",color="yellow")
    )

ft.app(target=main, assets_dir="assets")