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
    b = ft.ElevatedButton(text="Registrar", on_click=register_user,width=page.width*0.3,color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), side=ft.BorderSide(color=ft.colors.BLACK, width=1)),)
    buttonLogin = ft.ElevatedButton(text="Ya estoy registrado",width=page.width*0.3,color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), side=ft.BorderSide(color=ft.colors.BLACK, width=1)),)
    img = ft.Image(
        src=f"Bitcoin.png",
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN,
    )
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
                height=None,
                content=img,
                margin=ft.margin.only(top=page.width*0.02,left=page.height*0.02)
            ),
            ft.Container(
                content=tet,
                alignment=ft.alignment.center
            ),
            ft.Container(
                margin=ft.margin.only(top=page.height * 0.03),
                content=ft.Column([tb1, tb2]),
                alignment=ft.alignment.center
            ),
            ft.Container(
                margin=ft.margin.only(top=15),
                content=ft.Column([b,]),
                alignment=ft.alignment.center
            ),
            ft.Container(
                margin=ft.margin.only(top=5),
                content=ft.Column([buttonLogin, t]),
                alignment=ft.alignment.center
            ),
            ],
        ),
         bgcolor=ft.Colors.GREY_200,
         border=ft.border.all(0.5, ft.Colors.BLACK)
    ),
        ],
    ),
    )
    page.add(main_container)
    ft.app(main)
