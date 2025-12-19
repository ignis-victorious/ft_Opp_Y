#
#  Import LIBRARIES
import flet as ft

#  Import FILES
from compoments import Header

#
#  ______________________


@ft.component
def App() -> ft.Column:
    health, set_health = ft.use_state(5)
    return ft.Column(
        controls=[
            Header(text="Awsome State Demo"),
            ft.Row(
                controls=[ft.Text(value=f"{health}"), ft.Button(content="+", on_click=lambda: set_health(health + 3))]
            ),
        ]
    )


ft.run(lambda page: page.render(component=App))  # type: ignore


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
