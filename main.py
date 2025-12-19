#
#  Import LIBRARIES
import flet as ft

#  Import FILES
from compoments import Header

#
#  ______________________


@ft.component
def App() -> ft.Text:
    return Header(text="Awsome Components Demo")
    # return ft.Text(value="Great Components!")


ft.run(lambda page: page.render(App))  # type: ignore


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
