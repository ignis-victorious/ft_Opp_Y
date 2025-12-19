#
#  Import LIBRARIES
import flet as ft

#  Import FILES
#
#  ______________________


@ft.component
def HealthDisplay(health: int) -> ft.Row:
    #  This code gives type hinting erros
    # health: str = str(object=health)
    # return ft.Text(value=health, size=100, color="pink")
    # Pass the conversion directly to the value argument
    # return ft.Text(value=str(object=health), size=100, color="pink")
    # Or better:
    return ft.Row(
        controls=[
            ft.Icon(icon=ft.Icons.FAVORITE, size=100, color="red"),
            ft.Text(value=f"{health}", size=100, color="pink"),
        ]
    )
