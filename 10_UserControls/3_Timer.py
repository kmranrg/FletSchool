import flet as ft
import time, threading

'''
Theory: User control provides life-cycle "hook" methods

1) did_mount() - called after the UserControl added to a page.
2) will_unmount() - called before the UserControl is removed from a page.

Theory: Daemon

1) In multitasking computer OS, a daemon is a computer program
    that runs as background process, rather than being under the
    direct control of an interactive user.
'''

class Countdown(ft.UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.myThread = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.myThread.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            time.sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = ft.Text()
        return self.countdown


def main(page: ft.Page):
    page.add(Countdown(120), Countdown(60))

ft.app(target=main)