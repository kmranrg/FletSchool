'''
Theory:

1) The mechanics of drag-and-drop is pretty simple - a user starts draggoing `Draggable`
    control and "drops" it on `DragTarget`.
2) If both draggable and drag target has the same `group` a drag target will call
    `on_accept` event handler and pass draggable control ID as event data.
3) In this case draggable serves as a source "data" from drag-and-drop operation.
'''

# let's implement the theory mentioned above

import flet as ft

def main(page: ft.Page):
    page.title = "Simple Drag N Drop App"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)

        # update the text inside draggable control
        src.content.content.value = "0"

        # update the text inside drag target control
        e.control.content.content.value = "1"

        # let's update the page
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center
                    )
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center
                    ),
                    on_accept=drag_accept
                )
            ]
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)

'''
NOTE:

1) The above code is working fine because `Draggable` and `DragTarger` have the same group.
2) If they have different groups, in that case, on_accept function will not get invoked.
'''