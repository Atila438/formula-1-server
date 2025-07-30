from flask import Flask, jsonify

app = Flask(__name__)

# Updated F1 drivers data with country
drivers = {
    "hamilton": {
        "name": "Lewis Hamilton",
        "team": "Mercedes",
        "wins": 103,
        "championships": 7,
        "country": "United Kingdom"
    },
    "verstappen": {
        "name": "Max Verstappen",
        "team": "Red Bull Racing",
        "wins": 61,
        "championships": 3,
        "country": "Netherlands"
    },
    "senna": {
        "name": "Ayrton Senna",
        "team": "McLaren",
        "wins": 41,
        "championships": 3,
        "country": "Brazil"
    },
    "lauda": {
        "name": "Niki Lauda",
        "team": "Ferrari / McLaren",
        "wins": 25,
        "championships": 3,
        "country": "Austria"
    },
    "antonelli": {
        "name": "Kimi Antonelli",
        "team": "Mercedes Junior Team",
        "wins": 0,
        "championships": 0,
        "country": "Italy"
    },
    "schumacher": {
        "name": "Michael Schumacher",
        "team": "Ferrari",
        "wins": 91,
        "championships": 7,
        "country": "Germany"
    },
    "vettel": {
        "name": "Sebastian Vettel",
        "team": "Red Bull Racing / Ferrari",
        "wins": 53,
        "championships": 4,
        "country": "Germany"
    },
}

# Home route
@app.route('/')
def home():
    return "<h2>F1 Driver Stats API </h2><p>Try /driver/senna or /drivers</p>"

# Route to get individual driver data
@app.route('/driver/<name>')
def get_driver(name):
    driver = drivers.get(name.lower())
    if driver:
        return jsonify(driver), 200
    else:
        return jsonify({"error": "Driver not found"}), 404

# New route to list all drivers
@app.route('/drivers')
def list_all_drivers():
    return jsonify(drivers), 200

if __name__ == '__main__':
    app.run(debug=True)