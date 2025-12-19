#
#  Import LIBRARIES
# import random

import flet as ft

#  Import FILES
# from compoments.colorful_blocks import colorful_blocks
from compoments.images import images

#
#  ______________________

print(f"There are {len(list(ft.Colors))} colors")


# def images() -> list[ft.Image]:
#     return [ft.Image(src=f"https://picsum.photos/seed/{i}/300/150") for i in range(1, 201)]


# def colorful_blocks() -> list[ft.Container]:
#     return [
#         ft.Container(
#             alignment=ft.Alignment.CENTER,
#             content=ft.Text(value=str(i), size=20),
#             expand=True,
#             bgcolor=random.choice(seq=list(ft.Colors)),
#             # bgcolor="blue",
#         )
#         for i in range(1, 251)
#     ]


@ft.component
def App() -> ft.GridView:
    return ft.GridView(
        expand=1,
        runs_count=5,
        child_aspect_ratio=1.5,
        spacing=5.0,
        run_spacing=5,
        controls=[
            # ft.Text(value="Hello"),
            # *colorful_blocks(),
            *images(),
        ],
    )


ft.run(lambda page: page.render(component=App), assets_dir="assets")  # type: ignore


# def main():
#     print("Hello from ft-opp-y!")


# if __name__ == "__main__":
#     main()

#
#  Import LIBRARIES
# import flet as ft
#  Import FILES
#
#  ______________________
