import pytest
from app import app as flask_app
from flask import request, jsonify
from models import App
from app import db


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200


# Example: Change the add-app endpoint to include more validation
@app.route("/add-app", methods=["POST"])
def add_app():
    data = request.json
    
    # Add more validation
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    if not all(k in data for k in ("app_name", "version")):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Add custom validation
    if len(data["app_name"]) < 3:
        return jsonify({"error": "App name must be at least 3 characters"}), 400
    
    new_app = App(
        app_name=data["app_name"],
        version=data["version"],
        description=data.get("description", "")
    )
    
    db.session.add(new_app)
    db.session.commit()
    
    return jsonify({"message": "App added successfully", "app": new_app.to_dict()}), 201
