#
#  Import LIBRARIES
import flet as ft

#  Import FILES
#
#  ______________________


@ft.component
def CakeButton(health: int, set_health) -> ft.Button:
    return ft.Button(
        height=100,
        content=ft.Image(src="22_cheesecake.png", height=100, width=100, fit=ft.BoxFit.FIT_HEIGHT),
        on_click=lambda _: set_health(health + 3),
    )
