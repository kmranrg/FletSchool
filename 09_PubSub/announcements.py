'''
In this section, we will build a simple announcement app.
'''

import flet as ft

def main(page: ft.Page):
    page.title = "Make Announcements"

    # subscribe to broadcase announcements
    def on_announcement(message):
        announcements.controls.append(ft.Text(message))
        page.update()
    page.pubsub.subscribe(on_announcement)

    def send_click(e):
        page.pubsub.send_all(f"{user.value}: {announcement.value}")
        # cleaning up the form
        announcement.value = ""
        page.update()

    announcements = ft.Column()
    user = ft.TextField(hint_text="author name...", width=150)
    announcement = ft.TextField(hint_text="announcement...", expand=True)
    send = ft.ElevatedButton("Send", on_click=send_click)
    page.add(
        announcements,
        ft.Row(
            controls=[
                user,
                announcement,
                send,
            ]
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)