from flask import Flask, render_template_string, request

app = Flask(__name__)

# Sample products
products = [
    {"name": "NaNa for Sale", "price": "$925", "image": "/static/images/nana.jpeg"},
   
]

# HTML Template
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Anime Figures Store</title>
    <style>
        body { font-family: Arial; text-align: center; background-color: #f5f5f5; }
        .product { display: inline-block; margin: 20px; border: 1px solid #ccc; padding: 10px; background: #fff; border-radius: 8px; }
        img { width: 150px; height: 200px; }
        form { margin-top: 30px; }
        input, textarea { padding: 5px; width: 300px; }
        input[type="submit"] { width: 100px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Welcome to Anime Figures Store!</h1>
    <h2>Our Products:</h2>
    {% for product in products %}
    <div class="product">
        <img src="{{ product.image }}" alt="{{ product.name }}">
        <h3>{{ product.name }}</h3>
        <p>Price: {{ product.price }}</p>
    </div>
    {% endfor %}

    <h2>Contact Us</h2>
    <form method="POST">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Message: <textarea name="message" required></textarea><br><br>
        <input type="submit" value="Send">
    </form>

    {% if message %}
        <h3>{{ message }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user_message = request.form["message"]
        message = f"Thank you, {name}! We received your message."
        print(f"Message from {name} ({email}): {user_message}")  # logs to server console
    return render_template_string(html, products=products, message=message)

if __name__ == "__main__":
    # Host 0.0.0.0 makes it accessible on the internet when deployed
    app.run(debug=True, host='0.0.0.0', port=5000)
