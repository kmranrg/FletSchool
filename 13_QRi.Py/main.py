import flet as ft
import qrcode
import cv2

def main(page: ft.Page):
    page.title = "QR Code Scanner and Generator"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'light'
    page.scroll = 'always'
    page.bgcolor = '#ffffff'
    page.window_bgcolor = '#522125'

    dlg = ft.AlertDialog(
        title=ft.Text('Scan QR Code',text_align='center'),
        content=ft.Image(src='qr/qrCode.jpg', width=200)
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
        
    def generate_qrCode(e):
        img = qrcode.make(str(user_content.value))
        img.save('assets/qr/qrCode.jpg')
        open_dlg(e)
        page.update()
    
    def scan_qrCode(e):
        img = str('assets/qr/qrCode.jpg')
        detector = cv2.QRCodeDetector()
        value, _, _ = detector.detectAndDecode(cv2.imread(img))
        show_qr_content.value = value
        page.update()


    user_content = ft.TextField(hint_text='please put the content to encrypt', border_radius=40, border_color='#522125',color='#522125')
    generate_button = ft.ElevatedButton("Generate", on_click=generate_qrCode,bgcolor='#522125',color=ft.colors.WHITE)

    show_qr_content = ft.Text(text_align='center')
    scan_button = ft.ElevatedButton("Scan QR",on_click=scan_qrCode,bgcolor='#522125',color=ft.colors.WHITE)

    page.add(
        ft.Row([
            ft.Column(),
            ft.Column([ft.Image(src='qrCodeCover.png', height=500)],horizontal_alignment='center',alignment='center'),
            ft.Column([
                ft.Image(src='logo/appLogo.png',width=150),
                ft.Container(height=20),
                user_content,
                generate_button,
                ft.Row([show_qr_content],alignment='center'),
                scan_button,
                ft.Container(height=20),
                ft.Text(value='Made by: Kumar Anurag',color='#522125',weight='bold')
            ],horizontal_alignment='center',alignment='center'),
        ],
        alignment='center',
        vertical_alignment='center'
        ),
    )

ft.app(target=main, assets_dir='assets')