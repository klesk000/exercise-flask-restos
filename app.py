from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/api")
def api_root():
    return jsonify({"restos": "http://127.0.0.1:5000/api/restos/"})

@app.route("/api/restos/<city>", methods=["GET"])
def api_restos():
    response = api.get (f"""area[name="{city}"]; node["amenity"="restaurant"](area);""")