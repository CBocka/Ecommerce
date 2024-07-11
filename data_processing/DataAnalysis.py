from pyspark.sql import DataFrame, SparkSession
from data_processing.DataProcessing import *
from pyspark.sql.functions import sum, desc, col, count


def best_selling_products(spark: SparkSession, database: str) -> DataFrame:
    df = create_dataframe_from_table(spark, database, "order_details")
    result = df.groupBy("pro_id").agg(sum("pro_quantity")).alias("times sold").orderBy(desc("sum(pro_quantity)")).limit(
        5)
    return result


def unsold_products(spark: SparkSession, database: str) -> DataFrame:
    products_df = create_dataframe_from_table(spark, database, "products")
    order_details_df = create_dataframe_from_table(spark, database, "order_details")
    result = products_df.join(order_details_df, products_df.pro_id == order_details_df.pro_id, "left") \
        .where(col("ord_id").isNull())

    return result


def products_by_category(spark: SparkSession, database: str) -> DataFrame:
    products_df = create_dataframe_from_table(spark, database, "products")
    product_categories_df = create_dataframe_from_table(spark, database, "product_categories")

    product_by_category = products_df.groupBy("cat_id").count().orderBy(col("cat_id"))
    result = (product_by_category.join(product_categories_df, ["cat_id"])
              .select(col("cat_id").alias("Category ID"), col("cat_name").alias("Category Name"), col("count").alias("Total Products"))
              .orderBy("cat_id"))

    return result
