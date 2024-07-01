from database.DatabaseConnection import *
from database.PopulateDatabase import *


def main():
    target_database = "ecommerce_preproduction"
    cnx = connect_to_mysql(host="localhost", port=3306, user="root", password="root", database=target_database)

    populate_warehouses_table(cnx, 20)
    populate_customers_table(cnx, 100)
    populate_product_categories_table(cnx)
    populate_products_table(cnx)
    populate_orders_table(cnx, 30)

    cnx.close()

    #spark = SparkSession.builder.appName("Proyecto Ecommerce").master("local[*]").getOrCreate()
    #spark.stop()


if __name__ == "__main__":
    main()
