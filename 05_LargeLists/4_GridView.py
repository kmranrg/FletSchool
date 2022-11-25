'''
In this section, we will print 5000 items using `GridView`.
'''

import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=2)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(2, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5)
            )
        )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)

'''
NOTE:

1) With GridView scrolling and window resizing are smooth and responsive!
2) You can specify either fixed number of rows or columns (runs) with runs_count 
    property or the maximum size of a "tile" with max_extent property, so the number of 
    runs can vary automatically. In our example we set the maximum tile size to 150 pixels 
    and set its shape to "square" with child_aspect_ratio=1. child_aspect_ratio is the 
    ratio of the cross-axis to the main-axis extent of each child. Try changing it to 0.5 
    or 2.
'''