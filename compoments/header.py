#
#  Import LIBRARIES
import flet as ft

#  Import FILES
#
#  ______________________


@ft.component
def Header(text: str) -> ft.Text:
    return ft.Text(value=text, size=40)
