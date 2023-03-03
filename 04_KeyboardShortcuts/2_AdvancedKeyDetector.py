import flet
from flet import Container, Page, Row, Text, border, colors, KeyboardEvent


class ButtonControl(Container):
    def __init__(self, text):
        super().__init__()
        self.content = Text(text, font_family="SunnyspellsRegular", style="titleLarge")
        self.border = border.all(1, colors.BLACK54)
        self.border_radius = 3
        self.bgcolor = "0x09000000"
        self.padding = 10
        self.visible = False


def main(page: Page):

    page.title = "Advanced Key Detector"
    page.theme_mode = "light"

    page.fonts = {
        "charmelade": "fonts/charmelade.otf",
        "SunnyspellsRegular": "fonts/SunnyspellsRegular-MV9ze.otf"
    }

    def on_keyboard(e: KeyboardEvent):
        key.content.value = "Space Bar" if e.key == " " else e.key
        key.visible = True
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        meta.visible = e.meta
        page.update()

    page.on_keyboard_event = on_keyboard

    key = ButtonControl("")
    shift = ButtonControl("Shift (⇧)")
    ctrl = ButtonControl("Control (⌃)")
    alt = ButtonControl("Alt/Option (⌥ )")
    meta = ButtonControl("Command (⌘)")

    page.spacing = 50
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Text("Advanced Key Detector", style="headlineLarge", font_family="charmelade"),
        Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys..."),
        Row([shift, ctrl, alt, meta, key], alignment="center"),
    )


flet.app(target=main, assets_dir="assets")