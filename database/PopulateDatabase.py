from faker import Faker
from database.DatabaseConnection import *
import random


def populate_warehouses_table(cnx, num_records: int):
    faker = Faker("es_ES")

    for _ in range(num_records):
        warehouse_name = faker.company()

        record = {
            "wrh_name": warehouse_name,
            "wrh_location": faker.city()
        }

        warehouse_id = insert_into_table(cnx, "warehouses", record)
        warehouse_name_for_email = ''.join(warehouse_name.split()).lower().replace(".", "")

        record2 = {
            "wrh_id": warehouse_id,
            "wrh_phone": faker.phone_number(),
            "wrh_email": f"{warehouse_name_for_email}@gmail.com"
        }

        insert_into_table(cnx, "warehouse_contact", record2)


def populate_product_categories_table(cnx):
    categories = [
        {"cat_name": "Electrónica", "cat_desc": "Productos electrónicos como teléfonos y computadoras"},
        {"cat_name": "Hogar", "cat_desc": "Productos para el hogar como muebles y electrodomésticos"},
        {"cat_name": "Ropa", "cat_desc": "Ropa y accesorios para hombres y mujeres"},
        {"cat_name": "Deportes", "cat_desc": "Artículos deportivos como balones y equipamiento"},
        {"cat_name": "Libros", "cat_desc": "Libros de diferentes géneros y autores"},
        {"cat_name": "Juguetes", "cat_desc": "Juguetes para niños de todas las edades"},
        {"cat_name": "Alimentación", "cat_desc": "Productos alimenticios y bebidas"},
        {"cat_name": "Salud y belleza", "cat_desc": "Productos relacionados con la salud y el cuidado personal"},
        {"cat_name": "Automotriz", "cat_desc": "Piezas y accesorios para automóviles"},
        {"cat_name": "Mascotas", "cat_desc": "Productos para el cuidado de mascotas"},
        {"cat_name": "Instrumentos musicales", "cat_desc": "Instrumentos y equipos musicales"},
        {"cat_name": "Arte y manualidades", "cat_desc": "Suministros para actividades artísticas y manuales"},
        {"cat_name": "Electrodomésticos", "cat_desc": "Electrodomésticos para el hogar"},
        {"cat_name": "Informática", "cat_desc": "Equipos y accesorios de informática"},
        {"cat_name": "Decoración", "cat_desc": "Artículos de decoración para el hogar"}
    ]

    for category in categories:
        insert_into_table(cnx, "product_categories", category)


def populate_products_table(cnx):
    products = [
        {"pro_name": "Smartphone", "pro_unit_price": 299.99, "pro_img": "smartphone.jpg", "cat_id": 1},
        {"pro_name": "Laptop", "pro_unit_price": 799.99, "pro_img": "laptop.jpg", "cat_id": 1},
        {"pro_name": "Sofá", "pro_unit_price": 499.99, "pro_img": "sofa.jpg", "cat_id": 2},
        {"pro_name": "Lavadora", "pro_unit_price": 349.99, "pro_img": "lavadora.jpg", "cat_id": 2},
        {"pro_name": "Camisa", "pro_unit_price": 29.99, "pro_img": "camisa.jpg", "cat_id": 3},
        {"pro_name": "Zapatos", "pro_unit_price": 59.99, "pro_img": "zapatos.jpg", "cat_id": 3},
        {"pro_name": "Balón de Fútbol", "pro_unit_price": 19.99, "pro_img": "balon_futbol.jpg", "cat_id": 4},
        {"pro_name": "Bicicleta", "pro_unit_price": 299.99, "pro_img": "bicicleta.jpg", "cat_id": 4},
        {"pro_name": "Novela", "pro_unit_price": 15.99, "pro_img": "novela.jpg", "cat_id": 5},
        {"pro_name": "Enciclopedia", "pro_unit_price": 49.99, "pro_img": "enciclopedia.jpg", "cat_id": 5},
        {"pro_name": "Muñeca", "pro_unit_price": 14.99, "pro_img": "muneca.jpg", "cat_id": 6},
        {"pro_name": "Juego de construcción", "pro_unit_price": 39.99, "pro_img": "juego_construccion.jpg", "cat_id": 6},
        {"pro_name": "Cereal", "pro_unit_price": 3.99, "pro_img": "cereal.jpg", "cat_id": 7},
        {"pro_name": "Jugo de Naranja", "pro_unit_price": 2.99, "pro_img": "jugo_naranja.jpg", "cat_id": 7},
        {"pro_name": "Champú", "pro_unit_price": 5.99, "pro_img": "champu.jpg", "cat_id": 8},
        {"pro_name": "Cremas hidratantes", "pro_unit_price": 12.99, "pro_img": "cremas_hidratantes.jpg", "cat_id": 8},
        {"pro_name": "Llantas", "pro_unit_price": 99.99, "pro_img": "llantas.jpg", "cat_id": 9},
        {"pro_name": "Aceite para motor", "pro_unit_price": 24.99, "pro_img": "aceite_motor.jpg", "cat_id": 9},
        {"pro_name": "Comida para perros", "pro_unit_price": 19.99, "pro_img": "comida_perros.jpg", "cat_id": 10},
        {"pro_name": "Juguete para gatos", "pro_unit_price": 9.99, "pro_img": "juguete_gatos.jpg", "cat_id": 10},
        {"pro_name": "Guitarra", "pro_unit_price": 199.99, "pro_img": "guitarra.jpg", "cat_id": 11},
        {"pro_name": "Teclado", "pro_unit_price": 299.99, "pro_img": "teclado.jpg", "cat_id": 11},
        {"pro_name": "Pinturas acrílicas", "pro_unit_price": 12.99, "pro_img": "pinturas_acrilicas.jpg", "cat_id": 12},
        {"pro_name": "Lienzos", "pro_unit_price": 24.99, "pro_img": "lienzos.jpg", "cat_id": 12},
        {"pro_name": "Microondas", "pro_unit_price": 99.99, "pro_img": "microondas.jpg", "cat_id": 13},
        {"pro_name": "Refrigerador", "pro_unit_price": 699.99, "pro_img": "refrigerador.jpg", "cat_id": 13},
        {"pro_name": "Monitor", "pro_unit_price": 149.99, "pro_img": "monitor.jpg", "cat_id": 14},
        {"pro_name": "Teclado y ratón", "pro_unit_price": 39.99, "pro_img": "teclado_raton.jpg", "cat_id": 14},
        {"pro_name": "Cuadro decorativo", "pro_unit_price": 29.99, "pro_img": "cuadro_decorativo.jpg", "cat_id": 15},
        {"pro_name": "Jarrón", "pro_unit_price": 19.99, "pro_img": "jarron.jpg", "cat_id": 15}
    ]

    warehouses = read_table(cnx, "warehouses")

    for product in products:
        product_id = insert_into_table(cnx, "products", product)
        record_inventory = {
            "wrh_id": random.randint(a=1, b=len(warehouses)),
            "pro_id": product_id,
            "inv_quantity": random.randint(a=0, b=1000)
        }
        insert_into_table(cnx, "inventory", record_inventory)

    product_descriptions = [
        {"pro_id": 1, "pro_desc": "Teléfono inteligente con pantalla de 6.5 pulgadas y cámara de alta resolución."},
        {"pro_id": 2, "pro_desc": "Laptop con procesador Intel Core i7 y 16GB de RAM, ideal para trabajo y entretenimiento."},
        {"pro_id": 3, "pro_desc": "Sofá de tres plazas con tapizado de tela, muy cómodo y elegante."},
        {"pro_id": 4, "pro_desc": "Lavadora de carga frontal con capacidad de 7kg, eficiente y silenciosa."},
        {"pro_id": 5, "pro_desc": "Camisa de algodón para hombre, disponible en varios colores."},
        {"pro_id": 6, "pro_desc": "Zapatos de cuero para mujer, perfectos para cualquier ocasión."},
        {"pro_id": 7, "pro_desc": "Balón de fútbol profesional, aprobado por la FIFA."},
        {"pro_id": 8, "pro_desc": "Bicicleta de montaña con marco de aluminio, ligera y resistente."},
        {"pro_id": 9, "pro_desc": "Novela de misterio que te mantendrá en vilo hasta la última página."},
        {"pro_id": 10, "pro_desc": "Enciclopedia completa con más de 5000 artículos de diversos temas."},
        {"pro_id": 11, "pro_desc": "Muñeca con vestido de princesa, ideal para niñas de 3 a 8 años."},
        {"pro_id": 12, "pro_desc": "Juego de construcción con 1000 piezas, fomenta la creatividad y la imaginación."},
        {"pro_id": 13, "pro_desc": "Cereal integral con alto contenido de fibra, perfecto para un desayuno saludable."},
        {"pro_id": 14, "pro_desc": "Jugo de naranja natural, sin conservantes ni colorantes."},
        {"pro_id": 15, "pro_desc": "Champú con extractos naturales, cuida y fortalece tu cabello."},
        {"pro_id": 16, "pro_desc": "Cremas hidratantes para rostro y cuerpo, dejan la piel suave y tersa."},
        {"pro_id": 17, "pro_desc": "Llantas para automóvil, ofrecen gran durabilidad y adherencia."},
        {"pro_id": 18, "pro_desc": "Aceite sintético para motor, mejora el rendimiento y protege el motor."},
        {"pro_id": 19, "pro_desc": "Comida para perros con alto contenido de proteínas, nutritiva y deliciosa."},
        {"pro_id": 20, "pro_desc": "Juguete interactivo para gatos, los mantiene activos y entretenidos."},
        {"pro_id": 21, "pro_desc": "Guitarra acústica de madera, ideal para principiantes y profesionales."},
        {"pro_id": 22, "pro_desc": "Teclado electrónico con 61 teclas, múltiples funciones y efectos de sonido."},
        {"pro_id": 23, "pro_desc": "Pinturas acrílicas de colores vivos, perfectas para todo tipo de proyectos artísticos."},
        {"pro_id": 24, "pro_desc": "Lienzos de alta calidad, ideales para pintura al óleo y acrílico."},
        {"pro_id": 25, "pro_desc": "Microondas con grill, rápido y eficiente para calentar y cocinar."},
        {"pro_id": 26, "pro_desc": "Refrigerador con sistema No Frost, gran capacidad y eficiencia energética."},
        {"pro_id": 27, "pro_desc": "Monitor LED de 24 pulgadas, alta resolución y colores vibrantes."},
        {"pro_id": 28, "pro_desc": "Teclado y ratón inalámbricos, comodidad y libertad de movimiento."},
        {"pro_id": 29, "pro_desc": "Cuadro decorativo con diseño moderno, perfecto para cualquier ambiente."},
        {"pro_id": 30, "pro_desc": "Jarrón de cerámica, elegante y decorativo."}
    ]

    for product in product_descriptions:
        insert_into_table(cnx, "product_description", product)


def populate_customers_table(cnx, num_records: int):
    faker = Faker("es_ES")

    for _ in range(num_records):
        cus_name = faker.name()
        cus_name_for_email = ''.join(cus_name.split()).lower().replace(".", "")

        record_customer = {
            "cus_type": faker.word(ext_word_list=("Invitado", "Usuario registrado")),
            "cus_name": cus_name,
            "cus_email": f"{cus_name_for_email}@gmail.com",
            "cus_phone": faker.phone_number()
        }

        cus_id = insert_into_table(cnx, "customers", record_customer)

        if record_customer.get("cus_type") == "Usuario registrado":
            record_account = {
                "acc_name": cus_name_for_email,
                "cus_id": cus_id,
                "acc_password": faker.password(length=8),
                "acc_email": record_customer.get("cus_email"),
                "acc_creation_date": faker.date_this_decade()
            }
            insert_into_table(cnx, "accounts", record_account)


def populate_orders_table(cnx, num_records: int):
    faker = Faker("es_ES")

    customers = read_table(cnx, "customers")
    products = read_table(cnx, "products")

    for _ in range(num_records):
        customers_ids = random.randint(a=1, b=len(customers))

        record_order = {
            "cus_id": customers_ids,
            "ord_date": faker.date_time_this_decade(),
            "ord_total": faker.pydecimal(left_digits=random.randint(a=1, b=8), right_digits=2, positive=True)
        }
        order_id = insert_into_table(cnx, "orders", record_order)

        products_ids = random.randint(a=1, b=len(products))

        record_order_details = {
            "ord_id": order_id,
            "pro_id": products_ids,
            "pro_subtotal": faker.pydecimal(left_digits=random.randint(a=1, b=8), right_digits=2, positive=True),
        }
        insert_into_table(cnx, "order_details", record_order_details)

