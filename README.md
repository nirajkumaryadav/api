# Flask API for App Management

This API allows you to manage application details including creating, retrieving, updating, and deleting app records.

## Features

- Create new app entries with name, version, description, and author
- Retrieve individual app details by ID
- Get a list of all apps
- Update existing app information
- Delete apps
- Web interface for basic navigation

## API Endpoints

| Endpoint | Method | Description | Required Parameters |
|----------|--------|-------------|---------------------|
| `/add-app` | POST | Add a new app | `app_name`, `version` |
| `/get-app/{id}` | GET | Retrieve app by ID | `id` (in URL) |
| `/get-all-apps` | GET | Retrieve all apps | None |
| `/update-app/{id}` | PUT | Update an app | `id` (in URL) |
| `/delete-app/{id}` | DELETE | Delete an app | `id` (in URL) |

## Setup and Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

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

### Get all apps
```bash
curl http://127.0.0.1:5000/get-all-apps
```

### Update an app
```bash
curl -X PUT http://127.0.0.1:5000/update-app/1 \
  -H "Content-Type: application/json" \
  -d '{"app_name": "Updated App", "version": "2.0.0", "description": "Updated description"}'
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
