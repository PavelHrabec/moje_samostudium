# answer1.py

import psycopg2
from psycopg2 import sql, errors
import sys

DB_NAME = "exam2"
DB_USER = "postgres"
DB_PASSWORD = "Pavel1"  # <- sem dej svoje skutečné heslo
DB_HOST = "localhost"
DB_PORT = "5432"

def create_database():
    try:
        # připojíme se k výchozí databázi 'postgres'
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # pokusíme se vytvořit novou databázi
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(DB_NAME)
        ))

        print(f"Databáze '{DB_NAME}' byla úspěšně vytvořena.")

    except errors.DuplicateDatabase:
        print(f"Databáze '{DB_NAME}' již existuje.")

    except psycopg2.OperationalError as e:
        print("Nepodařilo se připojit k databázi.")
        print(f"Chyba: {e}")
        sys.exit(1)

    except Exception as e:
        print("Došlo k jiné chybě:")
        print(e)
        sys.exit(1)

    finally:
        # zavřeme spojení
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    create_database()