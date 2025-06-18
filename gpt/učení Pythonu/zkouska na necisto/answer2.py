# Vytvoření tabulky Users (email unikátní)
query_1 = """
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    password VARCHAR(60)
);
"""

# Vytvoření tabulky Messages s FK na Users (vztah 1:N)
query_2 = """
CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    message TEXT
);
"""

# Vytvoření tabulky Items
query_3 = """
CREATE TABLE Items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    description TEXT,
    price DECIMAL(7,2)
);
"""

# Vytvoření tabulky Orders
query_4 = """
CREATE TABLE Orders (
    id SERIAL PRIMARY KEY,
    description TEXT
);
"""

# Vytvoření tabulky spojující N:N vztah mezi Items a Orders
query_5 = """
CREATE TABLE ItemsOrders (
    item_id INTEGER REFERENCES Items(id),
    order_id INTEGER REFERENCES Orders(id),
    PRIMARY KEY (item_id, order_id)
);
"""

# Výběr všech položek (Items) s cenou vyšší než 13
query_6 = """
SELECT * FROM Items WHERE price > 13;
"""

# Vložení nové objednávky s popisem "popis vzorku"
query_7 = """
INSERT INTO Orders (description) VALUES ('popis vzorku');
"""

# Odstranění uživatele s id=7
query_8 = """
DELETE FROM Users WHERE id = 7;
"""

# Výběr všech uživatelů, kteří mají přiřazenou nějakou zprávu v Messages
query_9 = """
SELECT DISTINCT Users.* 
FROM Users
JOIN Messages ON Users.id = Messages.user_id;
"""

# Přidání sloupce date_of_created do tabulky Messages,
# který automaticky při vložení nastaví aktuální datum,
# a může obsahovat NULL pro starší záznamy
query_10 = """
ALTER TABLE Messages
ADD COLUMN date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
"""
