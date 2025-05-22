# Task Management API

A simple RESTful API for managing tasks, built with Flask and Python.

## Features

- Create new tasks
- Get all tasks
- Get a specific task
- Update tasks
- Delete tasks
- Unit tests with one intentionally failing test for CI/CD demonstration

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application:
```bash
python app.py
```

The server will start at `http://localhost:5000`

## API Endpoints

- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `GET /tasks/<task_id>` - Get a specific task
- `PUT /tasks/<task_id>` - Update a task
- `DELETE /tasks/<task_id>` - Delete a task

## Running Tests

To run the tests:
```bash
python -m unittest test_app.py
```

Note: There is one intentionally failing test (`test_intentionally_failing_test`) to demonstrate CI/CD failure scenarios.

## Example Usage

Create a new task:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"My Task","description":"Task description"}' http://localhost:5000/tasks
```

Get all tasks:
```bash
curl http://localhost:5000/tasks
```

Get a specific task:
```bash
curl http://localhost:5000/tasks/1
```

Update a task:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Task","completed":true}' http://localhost:5000/tasks/1
```

Delete a task:
```bash
curl -X DELETE http://localhost:5000/tasks/1
``` 