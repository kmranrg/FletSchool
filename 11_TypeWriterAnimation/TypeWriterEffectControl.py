import flet as ft
import time

class TypeWriterControl(ft.UserControl):
    def __init__(self, text_to_print):
        super().__init__()
        self.text_to_print = text_to_print

    def effect(self,e):
        for i in range(len(self.text_to_print)):
            self.my_type_writter_text.value += self.text_to_print[i] + "_"
            self.my_type_writter_text.update()
            self.my_type_writter_text.value = self.my_type_writter_text.value[:-1]
            time.sleep(0.02)
    
    def build(self):
        self.my_type_writter_text = ft.Text('My Typewriter Effect Will Happen Here!\n', no_wrap=False)
        return ft.Column([self.my_type_writter_text,ft.ElevatedButton("start effect", on_click=self.effect)])