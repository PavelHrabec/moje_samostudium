...
@app.route("/add_product", methods=("GET", "POST"))
def add_product_view():
    if request.method == "GET":
        return FORM
    else:
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        try:
            connection = connect(database="exam2", user="postgres", password="coderslab", host="127.0.0.1")
            connection.autocommit = True
            cursor = connection.cursor()
            save_product(cursor, name, description, price)
            connection.close()
            return "Product added!"
        except OperationalError as err:
            return err
