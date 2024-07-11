from pyspark.sql import SparkSession, DataFrame


def create_spark_session(name: str):
    spark = (SparkSession.builder
             .appName(name)
             .master("local[*]")
             .config("spark.driver.extraClassPath", "mysql-connector-j-8.1.0.jar")
             .getOrCreate())
    return spark


def set_logging_level(spark: SparkSession):
    spark.sparkContext.setLogLevel("ERROR")


def create_dataframe_from_table(spark: SparkSession, database: str, table: str):
    dataframe = (spark.read.format("jdbc")
                 .option("url", f"jdbc:mysql://localhost/{database}")
                 .option("driver", "com.mysql.cj.jdbc.Driver")
                 .option("dbtable", table)
                 .option("user", "root")
                 .option("password", "root")
                 .load()
                 )
    return dataframe


def save_dataframe_as_table(df: DataFrame, database: str, table: str):
    (df.write.format("jdbc")
     .option("url", f"jdbc:mysql://localhost/{database}")
     .option("driver", "com.mysql.cj.jdbc.Driver")
     .option("dbtable", f"{table}")
     .mode("append")
     .option("user", "root")
     .option("password", "root")
     .save()
     )


def close_session(spark: SparkSession):
    spark.stop()
