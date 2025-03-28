import json
import pytest
from app import app as flask_app
from models import db, App

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    
    with flask_app.app_context():
        db.create_all()
        
    yield flask_app
    
    with flask_app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_app(client):
    # Test adding a new app
    response = client.post("/add-app", 
                         data=json.dumps({
                             "app_name": "Test App", 
                             "version": "1.0.0", 
                             "description": "Test description"
                         }),
                         content_type='application/json')
    
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data["app"]["app_name"] == "Test App"
    assert data["app"]["version"] == "1.0.0"
    
def test_get_app(client):
    # First add an app
    response = client.post("/add-app", 
                         data=json.dumps({
                             "app_name": "Test App", 
                             "version": "1.0.0"
                         }),
                         content_type='application/json')
    data = json.loads(response.data)
    app_id = data["app"]["id"]
    
    # Then retrieve it
    response = client.get(f"/get-app/{app_id}")
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data["app_name"] == "Test App"
    
def test_delete_app(client):
    # First add an app
    response = client.post("/add-app", 
                         data=json.dumps({
                             "app_name": "Test App", 
                             "version": "1.0.0"
                         }),
                         content_type='application/json')
    data = json.loads(response.data)
    app_id = data["app"]["id"]
    
    # Then delete it
    response = client.delete(f"/delete-app/{app_id}")
    assert response.status_code == 200
    
    # Verify it's deleted
    response = client.get(f"/get-app/{app_id}")
    assert response.status_code == 404