# Proyecto Gestión de Ecommerce

Proyecto realizado con Python y PySpark como simulación de gestión para los datos generados por un comercio online.

### 1. Elaboración del esquema para la base de datos:

<p align="center">
<img src="https://github.com/user-attachments/assets/f84f7880-d000-490a-b343-f4f19b0d179f" height="450" width="700" >
</p>

El primer paso fue decidir la que sería la estructura de tablas para las bases de datos. Contamos con una base de datos de pre-producción y otra de producción. La estructura de tablas es la misma en ambas pero en producción únicamente podemos tener datos limpios y formateados de manera correcta.

Las bases de datos fueron creadas en local en MySQL.


### 2. Creación de las tablas:

Con las bases de datos creadas y el esquema de tablas decididas, toca crear dichas tablas. En el fichero de "create table sentences.txt" podemos ver las sentencias que fueron usadas para crear cada tabla y sus relaciones definidas en el esquema.


### 3. Funcionalidad para gestión de las tablas desde código:

Dentro del package database encontramos el fichero python de DatabaseConnection. En este fichero disponemos de una clase con una serie de funciones para gestión de tablas en una base de datos MySQL disponibles para ser usadas desde cualquier parte del programa.

Podemos realizar una conexión a una base de datos o cerrarla. Podemos leer, insertar, eliminar y actualizar registros de las tablas.

Se ha utilizado el package de mysql.connector


### 4. Poblar las tablas con datos ficticios de muestra:

Dentro del package database disponemos del fichero PopulateDatabase que cuenta con métodos para rellenar las tablas de nuestras bases de datos con registros ficticios.

Para algunos campos se ha utilizado la librería Faker de Python.

La documentación oficial se puede consultar [aquí](hthttps://faker.readthedocs.io/en/master/tp:// "aquí")


### 5. Uso de Apache Spark para limpiado y tratamiento de datos de las tablas:

Además del package database contamos con otro, data_processing. En él disponemos de ficheros python con clases y funciones para trabajar con PySpark en nuestro proyecto. 

El fichero DataProcessing contiene funciones básicas para crear una sesión de Spark (SparkSession), cerrar dicha sesión, crear un DataFrame a partir de una tabla de nuestra base de datos y persistir un DataFrame en una tabla.

Lo primero que hacemos es tratar algunos de los datos en las tablas de la base de datos de pre-producción para que sean adecuados para pasar a producción. 

Las funciones para el tratamiento de tablas lo encontramos en el fichero TableTreatment. Hemos decidido hacer algunos tratamientos como formatear los campos de teléfono, normalizar el texto de los campos de email o hashear los campos de contraseñas.

Para la limpieza de tablas procedemos de la siguiente manera. 
- Cargamos las tablas de la base de datos de pre-producción en DataFrames en memoria. 
- Usamos nuestras funciones sobre dichos DataFrames para realizar en ellos las modificaciones necesarias.
- Una vez que los datos son adecuados, guardamos el DataFrame como tabla en la base de datos de producción.


### 6. Uso de Apache Spark para obtener  información y agregaciones sobre nuestros datos:

Usamos las funciones definidas en el fichero DataAnalysis dentro del package data_processing para obtener información valiosa de nuestras tablas de producción. Las posibilidades aquí son infinitas, pero se han llevado a cabo tres estudios simples como ejemplo. Podemos consultar, por ejemplo, los productos más vendidos, los productos que nunca han sido comprados o el número de productos existentes por cada categoría, entre otras muchas posibilidades.

