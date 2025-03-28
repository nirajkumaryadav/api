# Flask API for App Management

This project provides a Flask API for managing app details, including adding, retrieving, and deleting apps.

## API Endpoints

- `POST /add-app`: Add app details to the database
- `GET /get-app/{id}`: Retrieve app details by ID
- `DELETE /delete-app/{id}`: Remove an app by ID

## Setup and Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd flask-template
```

2. Create a virtual environment and install dependencies:
```bash
# Using Python's built-in venv
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
flask run
```
Or use VS Code's Run and Debug functionality.

## Using the API

### Add a new app
```bash
curl -X POST http://127.0.0.1:5000/add-app \
  -H "Content-Type: application/json" \
  -d '{"app_name": "My App", "version": "1.0.0", "description": "This is my app"}'
```

### Get app details
```bash
curl http://127.0.0.1:5000/get-app/1
```

### Delete an app
```bash
curl -X DELETE http://127.0.0.1:5000/delete-app/1
```

## Testing

Run tests using pytest:
```bash
pytest
```

## Project Structure

- `app.py`: Main application file with API routes
- `models.py`: Database models for app data
- `templates/`: HTML templates for web interface
- `static/`: CSS and other static files
- `tests/`: Test files for the application
