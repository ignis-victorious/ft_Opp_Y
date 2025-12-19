#
#  Import LIBRARIES
import random

import flet as ft

#  Import FILES
#
#  ______________________


def colorful_blocks() -> list[ft.Container]:
    return [
        ft.Container(
            alignment=ft.Alignment.CENTER,
            content=ft.Text(value=str(i), size=20),
            expand=True,
            bgcolor=random.choice(seq=list(ft.Colors)),
            # bgcolor="blue",
        )
        for i in range(1, 251)
    ]
