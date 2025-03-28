# Flask API for App Management

A robust REST API built with Flask for managing application details, supporting complete CRUD operations with SQLite database storage and migration management.

## Features

- **Complete CRUD Operations**:
  - Create new app entries with name, version, description, and author
  - Retrieve individual app details by ID
  - Get a list of all apps
  - Update existing app information
  - Delete apps
- **Advanced Data Validation**: Automatic validation of inputs with sensible defaults
- **Database Features**: 
  - SQLite database with migration support
  - Indexed fields for performance
  - Relationship modeling for app versions
- **Environment Configuration**: Development, testing, and production environments
- **Web Interface**: Basic navigation UI for demonstration
- **Error Handling**: Comprehensive error handling and logging

## API Endpoints

| Endpoint | Method | Description | Required Parameters | Optional Parameters |
|----------|--------|-------------|---------------------|---------------------|
| `/add-app` | POST | Add a new app | `app_name`, `version` | `description`, `author` |
| `/get-app/{id}` | GET | Retrieve app by ID | `id` (in URL) | None |
| `/get-all-apps` | GET | Retrieve all apps | None | None |
| `/update-app/{id}` | PUT | Update an app | `id` (in URL) | `app_name`, `version`, `description`, `author` |
| `/delete-app/{id}` | DELETE | Delete an app | `id` (in URL) | None |

## Database Schema

### App Table
- `id`: Integer, Primary Key
- `app_name`: String(100), Not Null, Indexed
- `version`: String(20), Not Null
- `description`: Text, Nullable
- `created_at`: DateTime, Default: Current timestamp, Indexed
- `author`: String(100), Nullable
- `updated_at`: DateTime, Auto-updates on change

### AppVersion Table (Relationship)
- `id`: Integer, Primary Key
- `app_id`: Integer, Foreign Key to App.id
- `version_number`: String(20), Not Null
- `release_date`: DateTime, Default: Current timestamp
- `release_notes`: Text, Nullable

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

3. Set up the database with migrations:
```bash
flask db init     # Only if migrations folder doesn't exist
flask db migrate  # Create migration script
flask db upgrade  # Apply migrations to the database
```

4. Run the Flask application:
```bash
# Development mode
set FLASK_ENV=development  # On Windows
export FLASK_ENV=development  # On Linux/Mac
flask run

# Or use default configuration
flask run
```
Or use VS Code's Run and Debug functionality.

## Using the API

### Add a new app
```bash
curl -X POST http://127.0.0.1:5000/add-app \
  -H "Content-Type: application/json" \
  -d '{"app_name": "My App", "version": "1.0.0", "description": "This is my app", "author": "John Doe"}'
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
  -d '{"app_name": "Updated App", "version": "2.0.0", "description": "Updated description", "author": "Jane Smith"}'
```

### Delete an app
```bash
curl -X DELETE http://127.0.0.1:5000/delete-app/1
```

## Testing

Run the test suite with pytest:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_api.py
```

## Environment Configuration

The application supports different environments:

- **Development**: Debug mode enabled, using SQLite database
- **Testing**: Using in-memory SQLite database
- **Production**: Using environment variable for database URL (configurable)

To set the environment:
```bash
set FLASK_ENV=development|testing|production  # Windows
export FLASK_ENV=development|testing|production  # Linux/Mac
```

## Project Structure

- `app.py`: Main application file with API routes and error handling
- `models.py`: Database models with validation and relationships
- `config.py`: Environment-specific configuration
- `templates/`: HTML templates for web interface
- `static/`: CSS and other static files
- `tests/`: Test files for the application
- `migrations/`: Database migration scripts

## Sample Data

After setting up, you can populate the database with sample data:

```bash
curl -X POST http://127.0.0.1:5000/add-app -H "Content-Type: application/json" -d '{"app_name": "Weather App", "version": "1.0.0", "description": "Real-time weather forecasts", "author": "John Smith"}'

curl -X POST http://127.0.0.1:5000/add-app -H "Content-Type: application/json" -d '{"app_name": "Task Manager", "version": "2.1.3", "description": "Productivity tool for task management", "author": "Jane Doe"}'

curl -X POST http://127.0.0.1:5000/add-app -H "Content-Type: application/json" -d '{"app_name": "Recipe Finder", "version": "0.9.5", "description": "Find recipes based on available ingredients", "author": "Chef Alex"}'
```
