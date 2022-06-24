from flask import Flask

app = Flask(__name__)


# fetch promos route
@app.route("/promos")
def hello_world():
    return {"promos": ["promo1", "promo2", "promo3", ]}


if __name__ == "__main__":
    app.run(debug=True)
