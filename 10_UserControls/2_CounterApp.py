import flet as ft

'''
Theory:

1) UserControl should call self.update() to push its 
    changes to a Flet page.

2) super().__init__() must be always 
    called in your own constructor.
'''

class Counter(ft.UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count

    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.text = ft.Text(str(self.counter))
        return ft.Row([self.text, ft.ElevatedButton("Add", on_click=self.add_click)])

def main(page: ft.Page):
    page.add(Counter(100), Counter(45))

ft.app(target=main)