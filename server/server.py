from flask import Flask, jsonify, request
import json

app = Flask(__name__)
data = None

# Load JSON data
with open("storage.json", "r") as f:
  data = json.load(f)

def save_data():
  with open("storage.json", "w") as f:
    json.dump(data, f, indent=4)

# Get all users
@app.route("/users")
def get_users():
  return jsonify(data["users"])

# Create a new user
@app.route("/users", methods=["POST"])
def create_user():
  new_user = request.get_json()  # Get user data from request body
  if not new_user or not all(key in new_user for key in ("name", "email", "age", "interests", "bio", "relationshipType")):
    return jsonify({"error": "Missing required fields"}), 400
  # Generate unique ID (example)
  new_user["id"] = len(data["users"]) + 1
  data["users"].append(new_user)
  save_data()
  return jsonify(new_user), 201  # Created status code

# Get a specific user by ID
@app.route("/users/<int:user_id>")
def get_user(user_id):
  user = [u for u in data["users"] if u["id"] == user_id]
  if not user:
    return jsonify({"error": "User not found"}), 404
  return jsonify(user[0])

# Edit a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
  updated_user = request.get_json()
  if not updated_user:
    return jsonify({"error": "Missing user data"}), 400
  user_index = [i for i, u in enumerate(data["users"]) if u["id"] == user_id]
  if not user_index:
    return jsonify({"error": "User not found"}), 404
  data["users"][user_index[0]] = updated_user
  save_data()
  return jsonify(updated_user), 200

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
  user_index = [i for i, u in enumerate(data["users"]) if u["id"] == user_id]
  if not user_index:
    return jsonify({"error": "User not found"}), 404
  del data["users"][user_index[0]]
  save_data()
  return jsonify({"message": "User deleted"}), 204  # No Content status code

if __name__ == "__main__":
  app.run(debug=True)
