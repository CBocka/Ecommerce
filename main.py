from database.DatabaseConnection import *
from database.PopulateDatabase import *


def main():
    target_database = "ecommerce_pre_produccion"
    cnx = connect_to_mysql(host="localhost", port=3306, user="root", password="root", database=target_database)

    populate_almacenes_table(cnx, 100)
    populate_clientes_table(cnx, 4000)
    populate_categorias_productos_table(cnx)
    populate_productos_table(cnx, 800)

    cnx.close()

    #spark = SparkSession.builder.appName("Proyecto Ecommerce").master("local[*]").getOrCreate()
    #spark.stop()


if __name__ == "__main__":
    main()
