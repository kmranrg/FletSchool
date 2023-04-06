import flet as ft

def main(page: ft.Page):
    page.title = "Pizza Delivery App"
    page.theme_mode = "light"

    page.fonts = {
        "TravelingTypewriter": "fonts/TravelingTypewriter.ttf"
    }

    email = ft.TextField(hint_text="email id...", width=300, border_radius=20)
    password = ft.TextField(hint_text="password...", width=300, border_radius=20, password=True)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Pizza Store"), bgcolor=ft.colors.BLUE_100),
                    email,
                    password,
                    ft.Container(height=10),
                    ft.ElevatedButton("Login", on_click=go_to_welcome),
                ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center",
                padding=50,
            )
        )
        if page.route == "/welcome" or page.route == "/welcome/order_summary":
            page.views.append(
                ft.View(
                    "/welcome",
                    [
                        ft.AppBar(title=ft.Text("Welcome to the Store"), bgcolor=ft.colors.BLUE_100),
                        ft.Row([ft.Image(src="images/tomato.png", width=300),ft.Image(src="images/onion.png", width=300)], alignment="center"),
                        ft.Row([ft.Image(src="images/capsicum.png", width=300),ft.Image(src="images/watermelon.png", width=300)], alignment="center"),
                        ft.Row([ft.ElevatedButton("Add all Pizzas to Cart!", on_click=lambda _: page.go("/welcome/order_summary")),ft.ElevatedButton("Back to Login Page", on_click=lambda _: page.go("/"))], alignment="center"),
                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )
        if page.route == "/welcome/order_summary":
            page.views.append(
                ft.View(
                    "/order_summary",
                    [
                        ft.AppBar(title=ft.Text("Order Summary"), bgcolor=ft.colors.BLUE_100),
                        ft.Text("-----------------------------------------------------------------------------------"),
                        ft.Row([ft.Text("ORDER DETAILS",font_family="TravelingTypewriter",weight="bold",style="titleLarge")],alignment="center"),
                        ft.Text("-----------------------------------------------------------------------------------"),
                        ft.Text("1. Tomato Pizza [1 Qty] = ₹ 200/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("2. Onion Pizza [1 Qty] = ₹ 250/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("3. Capsicum Pizza [1 Qty] = ₹ 250/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("4. Watermelon Pizza [1 Qty] = ₹ 200/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("First order free delivery = ₹ 0/-",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("-----------------------------------------------------------------------------------"),
                        ft.Text("Total Payable Amount = ₹ 900/-",weight="bold",font_family="TravelingTypewriter",style="titleMedium"),
                        ft.Text("-----------------------------------------------------------------------------------"),
                        ft.Container(height=50),
                        ft.ElevatedButton("Back to Homepage", on_click=lambda _: page.go("/welcome")),
                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                    padding=50,
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def go_to_welcome(e):
        email.error_text = ""
        password.error_text = ""
        if not email.value:
            email.error_text = "missing email..."
            page.update()
        elif not password.value:
            password.error_text = "missing password..."
            page.update()
        else:
            page.go("/welcome")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")