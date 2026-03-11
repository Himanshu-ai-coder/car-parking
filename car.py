
from flask import Flask, render_template

car = Flask(__name__)

@car.route("/")
def home():
    return render_template("index.html")


@car.route("/search")
def search():
    return render_template("search.html")

@car.route("/car")
def car_page():
    return render_template("car.html")


@car.route("/bus")
def bus_page():
    return render_template("bus.html")



@car.route("/motorcycle")
def motorcycle_page():
    return render_template("motorcycle.html")


@car.route("/commercial")
def commercial_page():
    return render_template("commercial.html")









if __name__ == "__main__":
    car.run(debug=True)



# 🔹 READ (GET)
@car.route("/search", methods=["GET"])
def get_search():
    return jsonify({"message": "Search page accessed successfully"})



# 🔹 READ (GET)
@car.route("/car", methods=["GET"])
def get_car():
    return jsonify({"message": "Car page accessed successfully"})
