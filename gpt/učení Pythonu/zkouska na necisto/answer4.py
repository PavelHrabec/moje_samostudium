from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

DB_NAME = "exam2"
DB_USER = "postgres"
DB_PASSWORD = "Pavel1"  # <- zadej své heslo
DB_HOST = "localhost"
DB_PORT = "5432"

form_html = """
<form method="POST">
  <label>Name: <input type="text" name="name"></label><br>
  <label>Description: <input type="text" name="description"></label><br>
  <label>Price: <input type="text" name="price"></label><br>
  <button type="submit">Add Product</button>
</form>
<p>{{ message }}</p>
"""

def insert_item(name, description, price):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Items (name, description, price) VALUES (%s, %s, %s)",
            (name, description, price)
        )
        conn.commit()
        return True
    except Exception as e:
        print("Chyba při vkládání do databáze:", e)
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        try:
            price_val = float(price)
            if name and description and price_val >= 0:
                success = insert_item(name, description, price_val)
                if success:
                    message = "Product added!"
                else:
                    message = "Invalid data!"
            else:
                message = "Invalid data!"
        except ValueError:
            message = "Invalid data!"

    return render_template_string(form_html, message=message)

if __name__ == "__main__":
    app.run(debug=True)
