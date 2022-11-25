'''
Theory:

1) `ListView` can either be vertical (default) or horizontal.
2) `ListView` items are displayed one after another in the scroll direction.
'''

# let's print 5000 messages using `ListView` this time

import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)

ft.app(target=main, view=ft.WEB_BROWSER)

'''
NOTE:

1) Using `ListView` we can notice that the speed of scrolling 
    is too good as compared to the previous case.
2) We used expand=True in ListView constructor. In order to function properly, 
    ListView must have a height (or width if horizontal) specified. You could set an 
    absolute size, e.g. ListView(height=300, spacing=10), but in the example above we 
    make ListView to take all available space on the page, i.e. expand. 
'''