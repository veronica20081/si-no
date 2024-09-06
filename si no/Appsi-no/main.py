import flet as ft 


def main(page: ft.page):
    page.title = "¿Me perdonas?"
    page.bgcolor="pink"
    page.horizontal_alignment=ft.CrossAxisA


    
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))


ft.app(main)
