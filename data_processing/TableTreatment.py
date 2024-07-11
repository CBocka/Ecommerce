from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace, col, when, hash, concat, lit, substring, date_format, to_date
from pyspark.sql.types import StringType


def normalize_text(df: DataFrame, col_name: str) -> DataFrame:
    replacements = [
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        ("ü", "u"),
        ("Ü", "U"),
        ("à", "a"),
        ("è", "e"),
        ("ì", "i"),
        ("ò", "o"),
        ("ù", "u"),
        ("À", "A"),
        ("È", "E"),
        ("Ì", "I"),
        ("Ò", "O"),
        ("Ù", "U"),
        ("&", "_")
    ]

    for old, new in replacements:
        df = df.withColumn(col_name, regexp_replace(col(col_name), old, new))

    return df


def hash_password(df: DataFrame, col_name: str) -> DataFrame:
    result = df.withColumn(col_name, hash(col(col_name)).cast(StringType()))
    return result


def phone_field_treatment(df: DataFrame, col_name: str) -> DataFrame:
    df_clean = df.withColumn(col_name, regexp_replace(col(col_name), "[^0-9\\+]", ""))
    df_clean = df_clean.withColumn(col_name, regexp_replace(col(col_name), "\\s+", ""))

    df_with_default_country = df_clean.withColumn(col_name,
                                                  when(
                                                      df_clean[col_name].startswith("+"),
                                                      df_clean[col_name]
                                                  ).otherwise(
                                                      concat(lit("+34"), df_clean[col_name])
                                                  )
                                                  )

    df_formatted = df_with_default_country.withColumn(col_name,
                                                      concat(
                                                          lit("+"),
                                                          substring(col(col_name), 2, 2),
                                                          lit(" "),
                                                          substring(col(col_name), 4, 3),
                                                          lit(" "),
                                                          substring(col(col_name), 7, 2),
                                                          lit(" "),
                                                          substring(col(col_name), 9, 2),
                                                          lit(" "),
                                                          substring(col(col_name), 11, 2)
                                                      )
                                                      )
    return df_formatted
