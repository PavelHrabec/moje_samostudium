import psycopg2
from psycopg2 import errors
import sys

# Nastavení připojení k databázi exam2
DB_NAME = "exam2"
DB_USER = "postgres"
DB_PASSWORD = "Pavel1"  # ← sem dej své heslo
DB_HOST = "localhost"
DB_PORT = "5432"

# Dotazy dle zadání
query_1 = """
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    password VARCHAR(60)
);
"""

query_2 = """
CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    message TEXT
);
"""

query_3 = """
CREATE TABLE Items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    description TEXT,
    price DECIMAL(7,2)
);
"""

query_4 = """
CREATE TABLE Orders (
    id SERIAL PRIMARY KEY,
    description TEXT
);
"""

query_5 = """
CREATE TABLE ItemsOrders (
    item_id INTEGER REFERENCES Items(id),
    order_id INTEGER REFERENCES Orders(id),
    PRIMARY KEY (item_id, order_id)
);
"""

query_6 = """
SELECT * FROM Items WHERE price > 13;
"""

query_7 = """
INSERT INTO Orders (description) VALUES ('popis vzorku');
"""

query_8 = """
DELETE FROM Users WHERE id = 7;
"""

query_9 = """
SELECT DISTINCT Users.* 
FROM Users
JOIN Messages ON Users.id = Messages.user_id;
"""

query_10 = """
ALTER TABLE Messages
ADD COLUMN IF NOT EXISTS date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
"""

queries = [
    ("Vytvářím tabulku Users", query_1),
    ("Vytvářím tabulku Messages", query_2),
    ("Vytvářím tabulku Items", query_3),
    ("Vytvářím tabulku Orders", query_4),
    ("Vytvářím spojovací tabulku ItemsOrders", query_5),
    ("Vkládám novou objednávku", query_7),
    ("Mažu uživatele s ID 7", query_8),
    ("Přidávám sloupec date_of_created do Messages", query_10),
]

select_queries = [
    ("Výpis položek s cenou > 13", query_6),
    ("Výpis uživatelů, kteří mají zprávy", query_9),
]

def execute_queries():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()

        for description, q in queries:
            print(f"\n▶ {description}...")
            try:
                cursor.execute(q)
                print("   ✅ OK")
            except errors.DuplicateTable:
                print("   ℹ️ Tabulka již existuje.")
            except errors.DuplicateColumn:
                print("   ℹ️ Sloupec již existuje.")
            except Exception as e:
                print(f"   ⚠️ Chyba: {e}")

        for description, q in select_queries:
            print(f"\n▶ {description}:")
            try:
                cursor.execute(q)
                rows = cursor.fetchall()
                for row in rows:
                    print("   ", row)
                if not rows:
                    print("   (žádné výsledky)")
            except Exception as e:
                print(f"   ⚠️ Chyba při SELECT: {e}")

    except Exception as e:
        print("Nepodařilo se připojit k databázi.")
        print(f"Chyba: {e}")
        sys.exit(1)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    execute_queries()
