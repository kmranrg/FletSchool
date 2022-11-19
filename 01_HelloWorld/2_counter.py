'''
In this section, we will make a counter fuction which will count till 10 seconds
'''

import flet as ft
from time import sleep

def main(page: ft.Page):
    text = ft.Text()
    page.add(text) # it's a shortcut for page.controls.append(t) and then page.update()
    for i in range(1,11):
        text.value = "Count " + str(i)
        page.update()
        sleep(1) # it will make the program sleep for 1 second

ft.app(target=main)