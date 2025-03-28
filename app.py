from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models import db, App
import os

# Add this at the beginning of your app.py to see where SQLite is looking for the database
print(f"Database path: {os.path.abspath('apps.db')}")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# API Endpoints
@app.route("/add-app", methods=["POST"])
def add_app():
    data = request.json
    
    if not data or not all(k in data for k in ("app_name", "version")):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_app = App(
        app_name=data["app_name"],
        version=data["version"],
        description=data.get("description", ""),
        author=data.get("author", "")  # Add this line to handle the author field
    )
    
    db.session.add(new_app)
    db.session.commit()
    
    return jsonify({"message": "App added successfully", "app": new_app.to_dict()}), 201

@app.route("/get-app/<int:id>", methods=["GET"])
def get_app(id):
    app_record = App.query.get(id)
    
    if not app_record:
        return jsonify({"error": "App not found"}), 404
    
    return jsonify(app_record.to_dict())

@app.route("/delete-app/<int:id>", methods=["DELETE"])
def delete_app(id):
    app_record = App.query.get(id)
    
    if not app_record:
        return jsonify({"error": "App not found"}), 404
    
    db.session.delete(app_record)
    db.session.commit()
    
    return jsonify({"message": "App deleted successfully"})

# Example: Add a new endpoint to get all apps
@app.route("/get-all-apps", methods=["GET"])
def get_all_apps():
    try:
        apps = App.query.all()
        return jsonify([app.to_dict() for app in apps])
    except Exception as e:
        app.logger.error(f"Error in get_all_apps: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Example: Add an endpoint to update an app
@app.route("/update-app/<int:id>", methods=["PUT"])
def update_app(id):
    app_record = App.query.get(id)
    
    if not app_record:
        return jsonify({"error": "App not found"}), 404
    
    data = request.json
    
    if "app_name" in data:
        app_record.app_name = data["app_name"]
    
    if "version" in data:
        app_record.version = data["version"]
    
    if "description" in data:
        app_record.description = data["description"]
    
    if "author" in data:
        app_record.author = data["author"]  # Add this line
    
    db.session.commit()
    
    return jsonify({"message": "App updated successfully", "app": app_record.to_dict()})

@app.errorhandler(500)
def handle_500(error):
    import traceback
    app.logger.error(traceback.format_exc())
    return jsonify({"error": "Internal server error", "details": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)
