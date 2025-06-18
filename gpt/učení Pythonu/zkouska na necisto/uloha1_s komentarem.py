# Importujeme potřebné moduly
import psycopg2  # hlavní knihovna pro práci s PostgreSQL
from psycopg2 import sql, errors  # pro bezpečné SQL a specifické chyby
import sys  # pro ukončení programu v případě chyby

# Nastavení připojení k PostgreSQL
DB_NAME = "exam2"         # Název nové databáze, kterou chceme vytvořit
DB_USER = "postgres"      # Uživatelské jméno pro připojení (obvykle "postgres")
DB_PASSWORD = "tvoje_heslo"  # SEM ZADEJ SVÉ SKUTEČNÉ HESLO
DB_HOST = "localhost"     # Server běží lokálně
DB_PORT = "5432"          # Výchozí port PostgreSQL

# Hlavní funkce, která se pokusí vytvořit databázi
def create_database():
    try:
        # Připojení k výchozí databázi "postgres"
        conn = psycopg2.connect(
            dbname="postgres",   # nemůžeme se připojit k neexistující databázi
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        # Vypneme transakce, protože CREATE DATABASE nelze spustit uvnitř transakce
        conn.autocommit = True
        cursor = conn.cursor()

        # Vytvoření databáze pomocí bezpečného způsobu (ochrana proti SQL injection)
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(DB_NAME)
        ))

        # Úspěšná hláška
        print(f"Databáze '{DB_NAME}' byla úspěšně vytvořena.")

    # Pokud databáze už existuje, zachytíme specifickou chybu
    except errors.DuplicateDatabase:
        print(f"Databáze '{DB_NAME}' již existuje.")

    # Pokud se nepodaří připojit k databázi (např. špatné heslo, vypnutý server)
    except psycopg2.OperationalError as e:
        print("Nepodařilo se připojit k databázi.")
        print(f"Chyba: {e}")
        sys.exit(1)

    # Všechny ostatní neočekávané chyby
    except Exception as e:
        print("Došlo k jiné chybě:")
        print(e)
        sys.exit(1)

    # Vždy zavřeme spojení a kurzor, pokud byly úspěšně vytvořeny
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Spuštění skriptu
if __name__ == "__main__":
    create_database()
