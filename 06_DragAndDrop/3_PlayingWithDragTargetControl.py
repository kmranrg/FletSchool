# let's build the same app again but this time we will draw a 
# border around the target which shows not it's ready to drop 
# the draggable content

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

        # reset border
        e.control.content.border = None

        # let's update the page
        page.update()

    def drag_will_accept(e):
        # yellow border when it's allowed to drop and blue when it's not
        e.control.content.border = ft.border.all(
            2, ft.colors.YELLOW_400 if e.data == "true" else ft.colors.BLUE_400
        )
        e.control.update()

    def drag_leave(e):
        # now we are removing the border once the content is dropped
        e.control.content.border = None
        e.control.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=100,
                        height=100,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center
                    ),
                    # `content_when_dragging` will execute when user drags the Draggable
                    content_when_dragging=ft.Container(
                        width=100,
                        height=100,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5
                    ),
                    content_feedback=ft.Text("1"), # this will show only "1" while dragging not the entire container (box)
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=100,
                        height=100,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave
                )
            ]
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)