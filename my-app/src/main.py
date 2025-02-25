import flet as ft
import pyrebase
import flet
from flet import *
import datetime
from functools import partial

from pygments.cmdline import main_inner
from pygments.lexer import default


#Acuerdate  de instalar firease pip install pyrebase
config = {
    "apiKey": "AIzaSyBUipaFuHqb9lewOkHtVBzRIAKZWInFtYY",
    "authDomain": "loginflet-7b2ce.firebaseapp.com",
    "projectId": "loginflet-7b2ce",
    "storageBucket": "loginflet-7b2ce.firebasestorage.app",
    "messagingSenderId": "195689109726",
    "appId": "1:195689109726:web:8ca22ccb29a2ae16d90a4f",
    "measurementId": "G-5XB4L59X9Y",
    "databaseURL": "",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def main(page: ft.Page):
    tet=ft.Text("Register", size=30,color='Blue')
    tb1 = ft.TextField(label="Mail",width=page.width* 0.3 )
    tb2 = ft.TextField(label="Password ", password=True, can_reveal_password=True,width=page.width* 0.3)
    t = ft.Text()
    def register_user(e):
        email = tb1.value
        password = tb2.value
        try:
            user = auth.create_user_with_email_and_password(email, password)
            t.value = "Usuario registrado exitosamente"
        except Exception as error:
            t.value = "No se ha podido registrar correctamente"
        page.update()
    b = ft.ElevatedButton(text="Registrar", on_click=register_user)
    main_container = ft.Container(
    height=page.height,
    width=page.width,
    margin=ft.margin.only(top=page.height * 0.15),
    alignment=ft.alignment.center,
    content=ft.Column(controls=[
     ft.Container(
        width=page.width*0.5,
        height=page.height*0.6,
        border_radius=60,
        content=ft.Column(controls=[
            ft.Container(
                width=None,
                margin=ft.margin.only(top=page.height * 0.1),
                content=tet,
                alignment=ft.alignment.center
            ),
            ft.Container(
                width=None,
                margin=ft.margin.only(top=page.height * 0.05),
                content=ft.Column([tb1, tb2, b, t]),
                alignment=ft.alignment.center
            )
            ],
        ),
        bgcolor=ft.Colors.CYAN_50,
        alignment=ft.alignment.center
    ),
        ],
    ),
    )
    page.add(main_container)
ft.app(main)
