from faker import Faker
from database.DatabaseConnection import *
import random


def populate_almacenes_table(cnx, num_records: int):
    faker = Faker("es_ES")

    for _ in range(num_records):
        almacen_name = faker.company()

        record = {
            "almc_nombre": almacen_name,
            "almc_ubicacion": faker.city()
        }

        almacen_id = insert_into_table(cnx, "almacenes", record)
        almacen_name_for_email = ''.join(almacen_name.split()).lower().replace(".", "")

        record2 = {
            "almc_id": almacen_id,
            "almc_tlf_contacto": faker.phone_number(),
            "almc_email_contacto": f"{almacen_name_for_email}@gmail.com"
        }

        insert_into_table(cnx, "almacen_contacto", record2)


def populate_categorias_productos_table(cnx):
    categorias = [
        {"cat_nombre": "Electrónica", "cat_desc": "Productos electrónicos como teléfonos y computadoras"},
        {"cat_nombre": "Hogar", "cat_desc": "Productos para el hogar como muebles y electrodomésticos"},
        {"cat_nombre": "Ropa", "cat_desc": "Ropa y accesorios para hombres y mujeres"},
        {"cat_nombre": "Deportes", "cat_desc": "Artículos deportivos como balones y equipamiento"},
        {"cat_nombre": "Libros", "cat_desc": "Libros de diferentes géneros y autores"},
        {"cat_nombre": "Juguetes", "cat_desc": "Juguetes para niños de todas las edades"},
        {"cat_nombre": "Alimentación", "cat_desc": "Productos alimenticios y bebidas"},
        {"cat_nombre": "Salud y belleza", "cat_desc": "Productos relacionados con la salud y el cuidado personal"},
        {"cat_nombre": "Automotriz", "cat_desc": "Piezas y accesorios para automóviles"},
        {"cat_nombre": "Mascotas", "cat_desc": "Productos para el cuidado de mascotas"},
        {"cat_nombre": "Instrumentos musicales", "cat_desc": "Instrumentos y equipos musicales"},
        {"cat_nombre": "Arte y manualidades", "cat_desc": "Suministros para actividades artísticas y manuales"},
        {"cat_nombre": "Electrodomésticos", "cat_desc": "Electrodomésticos para el hogar"},
        {"cat_nombre": "Informática", "cat_desc": "Equipos y accesorios de informática"},
        {"cat_nombre": "Decoración", "cat_desc": "Artículos de decoración para el hogar"}
    ]

    for categoria in categorias:
        insert_into_table(cnx, "categorias_productos", categoria)


def populate_productos_table(cnx, num_records: int):
    faker = Faker("es_ES")

    categorias = read_table(cnx, "categorias_productos")
    almacenes = read_table(cnx, "almacenes")

    for _ in range(num_records):
        categoria_ids = random.randint(a=1, b=len(categorias))

        record_producto = {
            "pro_nombre": faker.word(),
            "pro_unit_precio": round(random.uniform(10.0, 1000.0), 2),
            "pro_img": faker.image_url(),
            "cat_id": categoria_ids
        }
        producto_id = insert_into_table(cnx, "productos", record_producto)

        descripcion_producto = faker.catch_phrase()

        record_descripcion = {
            "pro_id": producto_id,
            "desc_producto": descripcion_producto
        }
        insert_into_table(cnx, "descripcion_producto", record_descripcion)

        record_inventario = {
            "almc_id": random.randint(a=1, b=len(almacenes)),
            "pro_id": producto_id,
            "inv_cantidad": random.randint(a=0, b=1000)
        }
        insert_into_table(cnx, "inventario", record_inventario)


def populate_clientes_table(cnx, num_records: int):
    faker = Faker("es_ES")

    for _ in range(num_records):
        cli_nombre = faker.name()
        cli_nombre_for_email = ''.join(cli_nombre.split()).lower().replace(".", "")

        record_cliente = {
            "cli_tipo": faker.word(ext_word_list=("Invitado", "Usuario registrado")),
            "cli_nombre": cli_nombre,
            "cli_email": f"{cli_nombre_for_email}@gmail.com",
            "cli_tlf": faker.phone_number()
        }

        cli_id = insert_into_table(cnx, "clientes", record_cliente)

        if record_cliente.get("cli_tipo") == "Usuario registrado":
            record_cuenta = {
                "acc_name": cli_nombre_for_email,
                "cli_id": cli_id,
                "acc_password": faker.password(length=8),
                "acc_email": record_cliente.get("cli_email"),
                "acc_creation_date": faker.date_this_decade()
            }
            insert_into_table(cnx, "cuentas", record_cuenta)


def populate_pedidos_table(cnx, num_records: int):
    faker = Faker("es_ES")

    categorias = read_table(cnx, "categorias_productos")
    almacenes = read_table(cnx, "almacenes")

    for _ in range(num_records):
        categoria_ids = random.randint(a=1, b=len(categorias))

        record_producto = {
            "pro_nombre": faker.word(),
            "pro_unit_precio": round(random.uniform(10.0, 1000.0), 2),
            "pro_img": faker.image_url(),
            "cat_id": categoria_ids
        }
        producto_id = insert_into_table(cnx, "productos", record_producto)

        descripcion_producto = faker.catch_phrase()

        record_descripcion = {
            "pro_id": producto_id,
            "desc_producto": descripcion_producto
        }
        insert_into_table(cnx, "descripcion_producto", record_descripcion)

        record_inventario = {
            "almc_id": random.randint(a=1, b=len(almacenes)),
            "pro_id": producto_id,
            "inv_cantidad": random.randint(a=0, b=1000)
        }
        insert_into_table(cnx, "inventario", record_inventario)

