import os

from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["myapp"]
users_collection = db["users"]


def insert_user(name: str, age: int) -> str:
    result = users_collection.insert_one({"name": name, "age": age})
    return str(result.inserted_id)


def get_all_names() -> list[str]:
    return [doc["name"] for doc in users_collection.find({}, {"name": 1, "_id": 0})]


def get_all_users() -> list[dict]:
    return list(users_collection.find({}, {"_id": 0}))


@app.route("/")
def index():
    try:
        names = get_all_names()
        return render_template("index.html", names=names)
    except PyMongoError:
        app.logger.exception("Error connecting to database")
        return "Unable to load names right now.", 500



@app.route("/add", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name", "").strip()
    age = data.get("age")

    if not name or age is None:
        return jsonify({"error": "Name and age are required"}), 400

    try:
        insert_user(name, int(age))
        return jsonify(
            {"message": f"Successfully inserted: {name}", "names": get_all_names()}
        )
    except PyMongoError:
        app.logger.exception("Database error while adding user")
        return jsonify({"error": "Database error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)

