#
#  Import LIBRARIES

import flet as ft

#  Import FILES
#
#  ______________________


def images() -> list[ft.Image]:
    return [ft.Image(src=f"https://picsum.photos/seed/{i}/300/150") for i in range(1, 201)]
