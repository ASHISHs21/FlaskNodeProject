from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os, uuid, hashlib, json

load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["flask_database"]
todo_collection = db["todos"]

@app.route("/")
def home():
    return jsonify({"message": "Flask backend running!"})

@app.route("/api", methods=["GET"])
def get_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    try:
        data = request.get_json()
        item_name = data.get("itemName")
        item_description = data.get("itemDescription")

        if not item_name or not item_description:
            return jsonify({"error": "Both itemName and itemDescription are required"}), 400

        item_uuid = str(uuid.uuid4())
        item_hash = hashlib.sha256(item_name.encode()).hexdigest()

        todo_collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description,
            "itemUUID": item_uuid,
            "itemHash": item_hash
        })

        return jsonify({
            "message": "To-Do item submitted successfully!",
            "itemName": item_name,
            "itemDescription": item_description,
            "itemUUID": item_uuid,
            "itemHash": item_hash
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
