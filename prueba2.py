import flet as ft

def main(page):
    page.adaptive = True
    page.window_height = 500
    page.window_width = 600
    page.bgcolor = None  # Fondo transparente para la página

    checkboxes_container = ft.Column()  # Usar Column para organizar los checkboxes verticalmente

    def agregar_click(e):
        if new_task.value.strip():  # Validación de que no esté vacío el campo
            cb = ft.Checkbox(label=new_task.value)

            def editar_edicion(ev):
                textfield.value = cb.label
                textfield.visible = True
                textfield.focus()
                textfield.update()

            def guardar_edicion(ev):
                cb.label = textfield.value
                textfield.visible = False
                textfield.update()
                page.update()

            def eliminar(ev):
                checkboxes_container.controls.remove(cb_container)
                page.update()

            textfield = ft.TextField(value=cb.label, visible=False, on_submit=guardar_edicion)

            cb_container = ft.Row([
                cb,
                textfield,
                ft.IconButton(icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE, on_click=editar_edicion, bgcolor="#FFD700"),  # Color dorado
                ft.IconButton(icon=ft.icons.REMOVE, on_click=eliminar, bgcolor="#FFD700")  # Color dorado
            ])
            checkboxes_container.controls.append(cb_container)
            new_task.value = ""  # Limpiar el campo de texto
            new_task.focus()
            page.update()

    new_task = ft.TextField(hint_text="Qué necesitas agregar?", width=300)
    logo = ft.Image(src="./logoBodega.png", width=150, height=150)
    header_text = ft.Text("Bienvenido a la app de lista de compras de la Bodega J", size=20, weight=ft.FontWeight.BOLD)
    header = ft.Row(
        [
            ft.Container(content=header_text, alignment=ft.alignment.center_left, expand=1),
            ft.Container(content=logo, alignment=ft.alignment.center)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Función para limpiar la lista de productos
    def limpiar(e):
        checkboxes_container.controls.clear()  # Limpiar los checkboxes
        page.update()

    # Fila con campo de texto y botón de agregar (con color dorado)
    input_row = ft.Row([
        new_task,
        ft.IconButton(icon=ft.icons.ADD, on_click=agregar_click, bgcolor="#D3BF43", icon_color="#000000")  # Botón "Agregar" en dorado
    ])
    
    limpiar_button = ft.ElevatedButton("Limpiar", on_click=limpiar, bgcolor="#D3BF43", color="#000000")

    content_container = ft.Container(
        content=ft.Column([
            header,
            ft.Divider(height=20),
            input_row,
            checkboxes_container,  # Donde se colocarán los checkboxes
            limpiar_button
        ]),
        expand=True,
        padding=20,
        alignment=ft.alignment.top_center,
        bgcolor=None
    )

    # Imagen de fondo
    background_image = ft.Image(src="./fondoNegroOpaco.jpeg", width=page.window_width, height=page.window_height, fit=ft.ImageFit.COVER)

    # Uso de Stack para superponer la imagen y el contenedor de controles
    page.add(
        ft.Stack(
            controls=[
                background_image, 
                content_container  
            ]
        )
    )

ft.app(main)
