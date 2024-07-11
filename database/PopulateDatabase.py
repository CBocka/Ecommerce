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
        {"pro_name": "Jarrón", "pro_unit_price": 19.99, "pro_img": "jarron.jpg", "cat_id": 15},
        {"pro_name": "Auriculares", "pro_unit_price": 79.99, "pro_img": "auriculares.jpg", "cat_id": 1},
        {"pro_name": "Tablet", "pro_unit_price": 199.99, "pro_img": "tablet.jpg", "cat_id": 1},
        {"pro_name": "Manta", "pro_unit_price": 49.99, "pro_img": "manta.jpg", "cat_id": 2},
        {"pro_name": "Mesa de comedor", "pro_unit_price": 599.99, "pro_img": "mesa_comedor.jpg", "cat_id": 2},
        {"pro_name": "Pantalones", "pro_unit_price": 39.99, "pro_img": "pantalones.jpg", "cat_id": 3},
        {"pro_name": "Vestido", "pro_unit_price": 79.99, "pro_img": "vestido.jpg", "cat_id": 3},
        {"pro_name": "Pelota de tenis", "pro_unit_price": 9.99, "pro_img": "pelota_tenis.jpg", "cat_id": 4},
        {"pro_name": "Raqueta de tenis", "pro_unit_price": 119.99, "pro_img": "raqueta_tenis.jpg", "cat_id": 4},
        {"pro_name": "Libro de cocina", "pro_unit_price": 25.99, "pro_img": "libro_cocina.jpg", "cat_id": 5},
        {"pro_name": "Libro de historia", "pro_unit_price": 29.99, "pro_img": "libro_historia.jpg", "cat_id": 5},
        {"pro_name": "Pelota de playa", "pro_unit_price": 5.99, "pro_img": "pelota_playa.jpg", "cat_id": 6},
        {"pro_name": "Coche de juguete", "pro_unit_price": 49.99, "pro_img": "coche_juguete.jpg", "cat_id": 6},
        {"pro_name": "Galletas", "pro_unit_price": 2.99, "pro_img": "galletas.jpg", "cat_id": 7},
        {"pro_name": "Refresco", "pro_unit_price": 1.99, "pro_img": "refresco.jpg", "cat_id": 7},
        {"pro_name": "Crema dental", "pro_unit_price": 3.99, "pro_img": "crema_dental.jpg", "cat_id": 8},
        {"pro_name": "Jabón líquido", "pro_unit_price": 4.99, "pro_img": "jabon_liquido.jpg", "cat_id": 8},
        {"pro_name": "Bujías", "pro_unit_price": 12.99, "pro_img": "bujias.jpg", "cat_id": 9},
        {"pro_name": "Filtro de aire", "pro_unit_price": 19.99, "pro_img": "filtro_aire.jpg", "cat_id": 9},
        {"pro_name": "Collar para perros", "pro_unit_price": 15.99, "pro_img": "collar_perros.jpg", "cat_id": 10},
        {"pro_name": "Arena para gatos", "pro_unit_price": 10.99, "pro_img": "arena_gatos.jpg", "cat_id": 10},
        {"pro_name": "Piano", "pro_unit_price": 999.99, "pro_img": "piano.jpg", "cat_id": 11},
        {"pro_name": "Batería", "pro_unit_price": 799.99, "pro_img": "bateria.jpg", "cat_id": 11},
        {"pro_name": "Arcilla", "pro_unit_price": 9.99, "pro_img": "arcilla.jpg", "cat_id": 12},
        {"pro_name": "Tijeras", "pro_unit_price": 5.99, "pro_img": "tijeras.jpg", "cat_id": 12},
        {"pro_name": "Plancha", "pro_unit_price": 49.99, "pro_img": "plancha.jpg", "cat_id": 13},
        {"pro_name": "Cafetera", "pro_unit_price": 59.99, "pro_img": "cafetera.jpg", "cat_id": 13},
        {"pro_name": "Disco duro", "pro_unit_price": 79.99, "pro_img": "disco_duro.jpg", "cat_id": 14},
        {"pro_name": "Router", "pro_unit_price": 49.99, "pro_img": "router.jpg", "cat_id": 14},
        {"pro_name": "Alfombra", "pro_unit_price": 99.99, "pro_img": "alfombra.jpg", "cat_id": 15},
        {"pro_name": "Cortinas", "pro_unit_price": 39.99, "pro_img": "cortinas.jpg", "cat_id": 15},
        {"pro_name": "Smartwatch", "pro_unit_price": 199.99, "pro_img": "smartwatch.jpg", "cat_id": 1},
        {"pro_name": "Cámara", "pro_unit_price": 499.99, "pro_img": "camara.jpg", "cat_id": 1},
        {"pro_name": "Cama", "pro_unit_price": 899.99, "pro_img": "cama.jpg", "cat_id": 2},
        {"pro_name": "Estantería", "pro_unit_price": 199.99, "pro_img": "estanteria.jpg", "cat_id": 2},
        {"pro_name": "Chaqueta", "pro_unit_price": 99.99, "pro_img": "chaqueta.jpg", "cat_id": 3},
        {"pro_name": "Falda", "pro_unit_price": 49.99, "pro_img": "falda.jpg", "cat_id": 3},
        {"pro_name": "Guantes de boxeo", "pro_unit_price": 59.99, "pro_img": "guantes_boxeo.jpg", "cat_id": 4},
        {"pro_name": "Cinta de correr", "pro_unit_price": 499.99, "pro_img": "cinta_correr.jpg", "cat_id": 4},
        {"pro_name": "Diccionario", "pro_unit_price": 19.99, "pro_img": "diccionario.jpg", "cat_id": 5},
        {"pro_name": "Cuentos para niños", "pro_unit_price": 12.99, "pro_img": "cuentos_ninos.jpg", "cat_id": 5},
        {"pro_name": "Robot de juguete", "pro_unit_price": 99.99, "pro_img": "robot_juguete.jpg", "cat_id": 6},
        {"pro_name": "Rompecabezas", "pro_unit_price": 14.99, "pro_img": "rompecabezas.jpg", "cat_id": 6},
        {"pro_name": "Té", "pro_unit_price": 4.99, "pro_img": "te.jpg", "cat_id": 7},
        {"pro_name": "Chocolate", "pro_unit_price": 3.99, "pro_img": "chocolate.jpg", "cat_id": 7},
        {"pro_name": "Loción corporal", "pro_unit_price": 9.99, "pro_img": "locion_corporal.jpg", "cat_id": 8},
        {"pro_name": "Desodorante", "pro_unit_price": 4.99, "pro_img": "desodorante.jpg", "cat_id": 8},
        {"pro_name": "Anticongelante", "pro_unit_price": 14.99, "pro_img": "anticongelante.jpg", "cat_id": 9},
        {"pro_name": "Amortiguadores", "pro_unit_price": 89.99, "pro_img": "amortiguadores.jpg", "cat_id": 9},
        {"pro_name": "Comedero para perros", "pro_unit_price": 9.99, "pro_img": "comedero_perros.jpg", "cat_id": 10},
        {"pro_name": "Rascador para gatos", "pro_unit_price": 29.99, "pro_img": "rascador_gatos.jpg", "cat_id": 10},
        {"pro_name": "Saxofón", "pro_unit_price": 499.99, "pro_img": "saxofon.jpg", "cat_id": 11},
        {"pro_name": "Flauta", "pro_unit_price": 99.99, "pro_img": "flauta.jpg", "cat_id": 11},
        {"pro_name": "Paleta de colores", "pro_unit_price": 14.99, "pro_img": "paleta_colores.jpg", "cat_id": 12},
        {"pro_name": "Pinceles", "pro_unit_price": 19.99, "pro_img": "pinceles.jpg", "cat_id": 12},
        {"pro_name": "Tostadora", "pro_unit_price": 29.99, "pro_img": "tostadora.jpg", "cat_id": 13},
        {"pro_name": "Ventilador", "pro_unit_price": 39.99, "pro_img": "ventilador.jpg", "cat_id": 13},
        {"pro_name": "Teclado mecánico", "pro_unit_price": 99.99, "pro_img": "teclado_mecanico.jpg", "cat_id": 14},
        {"pro_name": "Impresora", "pro_unit_price": 129.99, "pro_img": "impresora.jpg", "cat_id": 14},
        {"pro_name": "Espejo", "pro_unit_price": 49.99, "pro_img": "espejo.jpg", "cat_id": 15},
        {"pro_name": "Lámpara de escritorio", "pro_unit_price": 29.99, "pro_img": "lampara_escritorio.jpg", "cat_id": 15}
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
        {"pro_id": 24, "pro_desc": "Lienzos de alta calidad, ideales para pintura al óleo y acrílica."},
        {"pro_id": 25, "pro_desc": "Microondas con función de descongelado rápido y grill."},
        {"pro_id": 26, "pro_desc": "Refrigerador de doble puerta con dispensador de agua y hielo."},
        {"pro_id": 27, "pro_desc": "Monitor de 24 pulgadas con resolución Full HD y tecnología anti-reflejo."},
        {"pro_id": 28, "pro_desc": "Teclado y ratón inalámbricos, cómodos y prácticos para trabajar desde casa."},
        {"pro_id": 29, "pro_desc": "Cuadro decorativo de paisaje, añade un toque de elegancia a tu hogar."},
        {"pro_id": 30, "pro_desc": "Jarrón de cerámica, ideal para flores frescas o secas."},
        {"pro_id": 31, "pro_desc": "Auriculares inalámbricos con cancelación de ruido, perfectos para música y llamadas."},
        {"pro_id": 32, "pro_desc": "Tablet de 10 pulgadas con pantalla HD y almacenamiento expandible."},
        {"pro_id": 33, "pro_desc": "Manta de lana suave y cálida, ideal para noches frías."},
        {"pro_id": 34, "pro_desc": "Mesa de comedor de madera maciza, perfecta para reuniones familiares."},
        {"pro_id": 35, "pro_desc": "Pantalones de mezclilla, cómodos y duraderos."},
        {"pro_id": 36, "pro_desc": "Vestido de verano, fresco y ligero, disponible en varios colores."},
        {"pro_id": 37, "pro_desc": "Pelota de tenis de alta calidad, aprobada por la ITF."},
        {"pro_id": 38, "pro_desc": "Raqueta de tenis profesional, ligera y resistente."},
        {"pro_id": 39, "pro_desc": "Libro de cocina con recetas fáciles y deliciosas para toda la familia."},
        {"pro_id": 40, "pro_desc": "Libro de historia mundial, una guía completa desde la prehistoria hasta la actualidad."},
        {"pro_id": 41, "pro_desc": "Pelota de playa inflable, perfecta para juegos en la arena."},
        {"pro_id": 42, "pro_desc": "Coche de juguete a escala, con luces y sonidos realistas."},
        {"pro_id": 43, "pro_desc": "Galletas de chocolate, crujientes y deliciosas."},
        {"pro_id": 44, "pro_desc": "Refresco de cola, refrescante y con el auténtico sabor de siempre."},
        {"pro_id": 45, "pro_desc": "Crema dental con flúor, protege contra las caries y fortalece el esmalte."},
        {"pro_id": 46, "pro_desc": "Jabón líquido antibacterial, elimina el 99.9% de las bacterias."},
        {"pro_id": 47, "pro_desc": "Bujías de alto rendimiento, mejora la combustión del motor."},
        {"pro_id": 48, "pro_desc": "Filtro de aire para coche, mantiene el motor limpio y eficiente."},
        {"pro_id": 49, "pro_desc": "Collar para perros ajustable, cómodo y resistente."},
        {"pro_id": 50, "pro_desc": "Arena para gatos, alta capacidad de absorción y control de olores."},
        {"pro_id": 51, "pro_desc": "Piano digital con teclado completo de 88 teclas y múltiples funciones."},
        {"pro_id": 52, "pro_desc": "Batería electrónica, ideal para practicar en casa sin hacer ruido."},
        {"pro_id": 53, "pro_desc": "Arcilla modelable, fácil de usar y apta para todas las edades."},
        {"pro_id": 54, "pro_desc": "Tijeras de precisión para manualidades, ergonómicas y afiladas."},
        {"pro_id": 55, "pro_desc": "Plancha de vapor con función de auto-limpieza y sistema anti-goteo."},
        {"pro_id": 56, "pro_desc": "Cafetera de cápsulas, prepara deliciosos cafés en segundos."},
        {"pro_id": 57, "pro_desc": "Disco duro externo de 1TB, ideal para almacenar grandes cantidades de datos."},
        {"pro_id": 58, "pro_desc": "Router inalámbrico de alta velocidad, ideal para streaming y gaming."},
        {"pro_id": 59, "pro_desc": "Alfombra de pelo largo, suave y acogedora."},
        {"pro_id": 60, "pro_desc": "Cortinas opacas, bloquean la luz y ofrecen privacidad."},
        {"pro_id": 61, "pro_desc": "Smartwatch con monitor de actividad, recibe notificaciones y controla tu salud."},
        {"pro_id": 62, "pro_desc": "Cámara digital de 20MP, captura fotos y videos en alta definición."},
        {"pro_id": 63, "pro_desc": "Cama de matrimonio con colchón ortopédico, para un descanso reparador."},
        {"pro_id": 64, "pro_desc": "Estantería modular, perfecta para organizar libros y decoraciones."},
        {"pro_id": 65, "pro_desc": "Chaqueta impermeable, ideal para días lluviosos."},
        {"pro_id": 66, "pro_desc": "Falda plisada, elegante y cómoda, disponible en varios colores."},
        {"pro_id": 67, "pro_desc": "Guantes de boxeo de cuero, duraderos y cómodos."},
        {"pro_id": 68, "pro_desc": "Cinta de correr plegable, perfecta para ejercitarse en casa."},
        {"pro_id": 69, "pro_desc": "Diccionario bilingüe, completo y actualizado."},
        {"pro_id": 70, "pro_desc": "Cuentos para niños con ilustraciones, ideal para antes de dormir."},
        {"pro_id": 71, "pro_desc": "Robot de juguete con control remoto, realiza múltiples funciones."},
        {"pro_id": 72, "pro_desc": "Rompecabezas de 1000 piezas, desafiante y divertido."},
        {"pro_id": 73, "pro_desc": "Té verde orgánico, antioxidante y saludable."},
        {"pro_id": 74, "pro_desc": "Chocolate negro, intenso y delicioso, elaborado con cacao de alta calidad."},
        {"pro_id": 75, "pro_desc": "Loción corporal hidratante, deja la piel suave y perfumada."},
        {"pro_id": 76, "pro_desc": "Desodorante en barra, protección eficaz durante todo el día."},
        {"pro_id": 77, "pro_desc": "Anticongelante para radiador, protege tu coche en temperaturas extremas."},
        {"pro_id": 78, "pro_desc": "Amortiguadores de alto rendimiento, mejora la estabilidad del vehículo."},
        {"pro_id": 79, "pro_desc": "Comedero para perros de acero inoxidable, fácil de limpiar."},
        {"pro_id": 80, "pro_desc": "Rascador para gatos, ideal para mantener sus uñas saludables."},
        {"pro_id": 81, "pro_desc": "Saxofón alto, perfecto para estudiantes y profesionales."},
        {"pro_id": 82, "pro_desc": "Flauta traversa de metal, sonido claro y brillante."},
        {"pro_id": 83, "pro_desc": "Paleta de colores para artistas, incluye una amplia gama de tonos."},
        {"pro_id": 84, "pro_desc": "Pinceles de diferentes tamaños, perfectos para todo tipo de técnicas."},
        {"pro_id": 85, "pro_desc": "Tostadora de acero inoxidable, con funciones de descongelado y recalentado."},
        {"pro_id": 86, "pro_desc": "Ventilador de torre, silencioso y eficiente, con control remoto."},
        {"pro_id": 87, "pro_desc": "Teclado mecánico retroiluminado, ideal para gamers y programadores."},
        {"pro_id": 88, "pro_desc": "Impresora multifuncional, imprime, escanea y copia con alta calidad."},
        {"pro_id": 89, "pro_desc": "Espejo de pared, elegante y moderno, con marco de madera."},
        {"pro_id": 90, "pro_desc": "Lámpara de escritorio LED, ajustable y con diferentes niveles de brillo."},
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
        customers_ids = random.randint(1, len(customers))

        ord_total_left_digits = random.randint(1, 4)
        ord_total_max_value = 10**ord_total_left_digits - 1

        record_order = {
            "cus_id": customers_ids,
            "ord_date": faker.date_time_this_decade(),
            "ord_total": faker.pydecimal(left_digits=ord_total_left_digits, positive=True, max_value=ord_total_max_value)
        }

        order_id = insert_into_table(cnx, "orders", record_order)

        products_ids = random.randint(1, len(products))

        pro_subtotal_left_digits = random.randint(1, 4)
        pro_subtotal_max_value = 10**pro_subtotal_left_digits - 1

        record_order_details = {
            "ord_id": order_id,
            "pro_id": products_ids,
            "pro_quantity": random.randint(1, 4),
            "pro_subtotal": faker.pydecimal(left_digits=pro_subtotal_left_digits, positive=True, max_value=pro_subtotal_max_value),
        }

        insert_into_table(cnx, "order_details", record_order_details)

