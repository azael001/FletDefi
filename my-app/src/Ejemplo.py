import flet as ft
import pyrebase
import flet
from flet import *
import datetime
from functools import partial
from pygments.cmdline import main_inner
from pygments.lexer import default


# Acuerdate  de instalar firebase pip install pyrebase4
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
    # Función para un correcto width del container
    if page.width < 500:
        container_width = page.width
    elif 500 <= page.width < 700:
        container_width = page.width * 0.7
    else:
        container_width = page.width * 0.5

    # Función Login
    def login_user(e):
        email = tb1.value
        password = tb2.value
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            page.go("/main")
        except Exception as error:
            t.value = "No se ha podido Loguear correctamente"
        page.update()

    # Función registro
    def register_user(e):
        email = tb1.value
        password = tb2.value
        try:
            user = auth.create_user_with_email_and_password(email, password)
            tb1.value=""
            tb2.value=""
            t.value="Usuario registrado correctamente.Introduzca mail y contraseña."
            page.go("/")
        except Exception as error:
            t.value = "No se ha podido registrar correctamente"
        page.update()

    # Componentes de Login
    tetLogin=ft.Text("Iniciar sesión", size=30,color='Blue')
    buttonRegister = ft.ElevatedButton(text="No estoy registrado", width=page.width * 0.3, color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),side=ft.BorderSide(color=ft.Colors.BLACK, width=1)),on_click=lambda e: page.go("/register"))
    blogin = ft.ElevatedButton(text="Loguearse", on_click=login_user, width=page.width * 0.3, color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),side=ft.BorderSide(color=ft.Colors.BLACK, width=1)), )

    # Componentes de Registro
    tet = ft.Text("Regsitrarse", size=30, color='Blue')
    t = ft.Text()
    b = ft.ElevatedButton(text="Registrar", on_click=register_user,width=page.width*0.3,color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), side=ft.BorderSide(color=ft.Colors.BLACK, width=1)),)
    buttonLogin = ft.ElevatedButton(text="Ya estoy registrado", width=page.width * 0.3, color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),side=ft.BorderSide(color=ft.Colors.BLACK, width=1)),on_click=lambda e: page.go("/"))

    ##Componentes comunes Login y registro
    tb1 = ft.TextField(label="Mail", width=page.width * 0.3)
    tb2 = ft.TextField(label="Password ", password=True, can_reveal_password=True, width=page.width * 0.3)
    img = ft.Image(src=f"Bitcoin.png",width=50,height=50,fit=ft.ImageFit.CONTAIN,)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Container(
                        height=page.height,
                        width=page.width,
                        margin=ft.margin.only(top=page.height * 0.15),
                        alignment=ft.alignment.center,
                        content=ft.Column(controls=[
                            ft.Container(
                                width=container_width,
                                height=page.height * 0.6,
                                border_radius=60,
                                content=ft.Column(controls=[
                                    ft.Container(
                                        width=None,
                                        height=None,
                                        content=img,
                                        margin=ft.margin.only(top=page.width * 0.02, left=page.height * 0.02)
                                    ),
                                    ft.Container(
                                        content=tetLogin,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Container(
                                        margin=ft.margin.only(top=page.height * 0.03),
                                        content=ft.Column([tb1, tb2]),
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Container(
                                        margin=ft.margin.only(top=15),
                                        content=ft.Column([blogin]),
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Container(
                                        margin=ft.margin.only(top=5),
                                        content=ft.Column([buttonRegister, t]),
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
                ],
            )
        )
        page.update()

        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        ft.Container(
                            height=page.height,
                            width=page.width,
                            margin=ft.margin.only(top=page.height * 0.15),
                            alignment=ft.alignment.center,
                            content=ft.Column(controls=[
                                ft.Container(
                                    width=container_width,
                                    height=page.height * 0.6,
                                    border_radius=60,
                                    content=ft.Column(controls=[
                                        ft.Container(
                                            width=None,
                                            height=None,
                                            content=img,
                                            margin=ft.margin.only(top=page.width * 0.02, left=page.height * 0.02)
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
                                            content=ft.Column([b, ]),
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
                    ],

                )

            )
            page.update()

        carrito = {}

        if page.route == "/main":
            productos = [
                {"nombre": "raton", "precio": 25, "stock": 255},
                {"nombre": "teclado", "precio": 45, "stock": 259},
                {"nombre": "casco", "precio": 30, "stock": 150},
                {"nombre": "pc", "precio": 550, "stock": 143},
                {"nombre": "mesa", "precio": 80, "stock": 220},
                {"nombre": "silla", "precio": 60, "stock":135},
                {"nombre": "reposapies", "precio": 20, "stock": 63},
                {"nombre": "microfono", "precio": 40, "stock": 139},
                {"nombre": "impresora", "precio": 100, "stock": 145},
                {"nombre": "pack-boligrafo", "precio": 5, "stock": 1110},
                {"nombre": "folios", "precio": 10, "stock": 500},
                {"nombre": "portatil", "precio": 750, "stock": 50}
            ]

            cart_column = ft.Column()

            def mostrar_carrito():
                resumen = []
                total = 0
                for nombre, datos in carrito.items():
                    subtotal = datos["precio"] * datos["cantidad"]
                    total += subtotal
                    resumen.append(
                        ft.Row(
                            controls=[
                                ft.Image(src=f"{nombre}.png", width=50, height=50),
                                ft.Text(
                                    f"{nombre.capitalize()}: {datos['cantidad']} x ${datos['precio']} = ${subtotal}")
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    )

                if not resumen:
                    resumen.append(ft.Text("El carrito está vacío."))
                resumen.append(ft.Text(f"Total: ${total}", weight="bold"))
                cart_column.controls = resumen
                page.update()

            def create_product(producto):
                name = producto["nombre"]
                precio = producto["precio"]
                stock = producto["stock"]
                image_path = f"{name}.png"

                cantidad_input = ft.TextField(
                    label="Cantidad",
                    width=100,
                    value="1",
                    keyboard_type=ft.KeyboardType.NUMBER
                )

                def agregar_al_carrito(e, producto_name=name, producto_precio=precio, producto_stock=stock):
                    cantidad = cantidad_input.value
                    if cantidad.isdigit() and int(cantidad) > 0:
                        cantidad = int(cantidad)
                        if producto_name in carrito:
                            nueva_cantidad = carrito[producto_name]["cantidad"] + cantidad
                            if nueva_cantidad > producto_stock:
                                print("Supera el stock disponible.")
                                return
                            carrito[producto_name]["cantidad"] = nueva_cantidad
                        else:
                            if cantidad > producto_stock:
                                print("No hay suficientes unidades disponibles.")
                                return
                            carrito[producto_name] = {
                                "precio": producto_precio,
                                "cantidad": cantidad
                            }
                        print(f"Agregado: {producto_name} ({cantidad})")
                        mostrar_carrito()
                    else:
                        print("Cantidad inválida")

                return ft.Container(
                    width=420,
                    height=450,
                    bgcolor=ft.Colors.GREY_200,
                    border_radius=10,
                    border=ft.border.all(1, ft.Colors.GREY_600),
                    padding=20,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Image(src=image_path, width=230, height=210, fit=ft.ImageFit.COVER)
                            ),
                            ft.Text(name.capitalize(), size=16, weight="bold"),
                            ft.Text(f"Precio: ${precio}"),
                            ft.Text(f"Unidades disponibles: {stock}"),
                            cantidad_input,
                            ft.ElevatedButton("Agregar al carrito", on_click=agregar_al_carrito)
                        ],
                        spacing=10
                    )
                )

            lista_productos = [create_product(p) for p in productos]

            rows = []
            products_per_row = 4
            for i in range(0, len(lista_productos), products_per_row):
                row_products = lista_productos[i:i + products_per_row]
                row = ft.Row(
                    controls=row_products,
                    alignment=ft.MainAxisAlignment.START,
                    spacing=40
                )
                rows.append(ft.Container(content=row, margin=ft.margin.only(bottom=30)))

            page.views.append(
                ft.View(
                    "/main",
                    controls=[
                        ft.AppBar(title=ft.Text("Almacen"), bgcolor=ft.Colors.BLUE),
                        ft.Container(
                            expand=True,
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.ListView(
                                        controls=rows,
                                        expand=True,
                                        padding=10
                                    ),
                                    ft.Divider(),
                                    ft.Text("Carrito ", size=18, weight="bold"),
                                    cart_column,
                                    ft.ElevatedButton(
                                        "Finalizar pedido",
                                        on_click=lambda e: (
                                            carrito.clear(),
                                            mostrar_carrito(),
                                            print("Pedido finalizado")
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
            page.update()

    ##Configuración del router
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)
