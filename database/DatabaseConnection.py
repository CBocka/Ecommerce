import mysql.connector as cpy
import logging


def connect_to_mysql(host, port, user, password, database):
    logging.basicConfig(level=logging.DEBUG)

    config = {
        "host": host,
        "port": port,
        "user": user,
        "password": password,
        "database": database,
        "use_pure": True
    }

    try:
        cnx = cpy.connect(**config)
        logging.info("Connected to MySQL successfully")
        return cnx
    except cpy.Error as err:
        logging.error(f"Error connecting to MySQL: {err}")
        return None


def close_connection(connection):
    connection.close()


def read_table(cnx, table_name, record_id=None):
    try:
        cursor = cnx.cursor(dictionary=True)

        if record_id is None:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
        else:
            query = f"SELECT * FROM {table_name} WHERE id = %s"
            cursor.execute(query, (record_id,))

        result = cursor.fetchall()
        return result

    except cpy.Error as err:
        logging.error(f"Error: {err}")
        return []

    finally:
        cursor.close()


def insert_into_table(cnx, table_name, data):
    try:
        cursor = cnx.cursor()
        placeholders = ", ".join(["%s"] * len(data))
        columns = ", ".join(data.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(data.values()))
        cnx.commit()
        logging.info("Insert successful")
    except cpy.Error as err:
        logging.error(f"Error: {err}")
    finally:
        cursor.close()

    return cursor.lastrowid


def update_table(cnx, table_name, data, condition):
    try:
        cursor = cnx.cursor()
        set_clause = ", ".join([f"{k}=%s" for k in data.keys()])
        condition_clause = " AND ".join([f"{k}=%s" for k in condition.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}"
        values = list(data.values()) + list(condition.values())
        cursor.execute(query, values)
        cnx.commit()
        logging.info("Update successful")
    except cpy.Error as err:
        logging.error(f"Error: {err}")
    finally:
        cursor.close()


def delete_from_table(cnx, table_name, condition):
    try:
        cursor = cnx.cursor()
        condition_clause = " AND ".join([f"{k}=%s" for k in condition.keys()])
        query = f"DELETE FROM {table_name} WHERE {condition_clause}"
        cursor.execute(query, list(condition.values()))
        cnx.commit()
        logging.info("Delete successful")
    except cpy.Error as err:
        logging.error(f"Error: {err}")
    finally:
        cursor.close()
