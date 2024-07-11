from data_processing.DataProcessing import *
from database.PopulateDatabase import *
from data_processing.TableTreatment import *
from data_processing.DataAnalysis import *


def main():
    logging.getLogger("mysql.connector").setLevel(logging.ERROR)
    logging.getLogger("py4j.clientserver").setLevel(logging.ERROR)

    input_database = "ecommerce_preproduction"
    output_database = "ecommerce_production"

    cnx = connect_to_mysql(host="localhost", port=3306, user="root", password="root", database=input_database)
    populate_database(cnx)
    close_connection(cnx)

    spark = create_spark_session("Ecommerce Project")
    set_logging_level(spark)

    tables_treatments(spark, input_database, output_database)
    analysis_from_production_tables(spark, output_database)

    close_session(spark)


def populate_database(cnx):
    populate_warehouses_table(cnx, 30)
    populate_product_categories_table(cnx)
    populate_products_table(cnx)
    populate_customers_table(cnx, 1000)
    populate_orders_table(cnx, 2000)


def tables_treatments(spark: SparkSession, input_database: str, output_database: str):
    warehouses_df = create_dataframe_from_table(spark, input_database, "warehouses")
    save_dataframe_as_table(warehouses_df, output_database, "warehouses")

    warehouse_contact_df = create_dataframe_from_table(spark, input_database, "warehouse_contact")
    warehouse_contact_df = phone_field_treatment(warehouse_contact_df, "wrh_phone")
    warehouse_contact_df = normalize_text(warehouse_contact_df, "wrh_email")
    save_dataframe_as_table(warehouse_contact_df, output_database, "warehouse_contact")

    product_categories_df = create_dataframe_from_table(spark, input_database, "product_categories")
    save_dataframe_as_table(product_categories_df, output_database, "product_categories")

    products_df = create_dataframe_from_table(spark, input_database, "products")
    save_dataframe_as_table(products_df, output_database, "products")

    product_description_df = create_dataframe_from_table(spark, input_database, "product_description")
    save_dataframe_as_table(product_description_df, output_database, "product_description")

    inventory_df = create_dataframe_from_table(spark, input_database, "inventory")
    save_dataframe_as_table(inventory_df, output_database, "inventory")

    customers_df = create_dataframe_from_table(spark, input_database, "customers")
    customers_df = phone_field_treatment(customers_df, "cus_phone")
    customers_df = normalize_text(customers_df, "cus_email")
    save_dataframe_as_table(customers_df, output_database, "customers")

    accounts_df = create_dataframe_from_table(spark, input_database, "accounts")
    accounts_df = hash_password(accounts_df, "acc_password")
    accounts_df = normalize_text(accounts_df, "acc_email")
    save_dataframe_as_table(accounts_df, output_database, "accounts")

    orders_df = create_dataframe_from_table(spark, input_database, "orders")
    save_dataframe_as_table(orders_df, output_database, "orders")

    order_details_df = create_dataframe_from_table(spark, input_database, "order_details")
    save_dataframe_as_table(order_details_df, output_database, "order_details")


def analysis_from_production_tables(spark: SparkSession, database: str):
    best_selling_products_df = best_selling_products(spark, database)
    best_selling_products_df.show(truncate=False)

    unsold_products_df = unsold_products(spark, database)
    unsold_products_df.show(truncate=False)

    products_by_category_df = products_by_category(spark, database)
    products_by_category_df.show()


if __name__ == "__main__":
    main()



