from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    prediction = round(random.uniform(1.00, 20.00), 2)
    return f"<h1 style='text-align:center;'>🚀 Aviator Predictor: <span style='color:red;'>{prediction}x</span></h1>"

if __name__ == "__main__":
    app.run(debug=True)
