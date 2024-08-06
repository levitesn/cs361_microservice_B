# FastAPI User Management Service

## Overview

This FastAPI microservice provides endpoints to create users and perform login operations. It uses a simple in-memory dictionary to store user credentials.

## Features

- Create a new user with a username and password.
- Login with a username and password to validate credentials.

## Endpoints

### Create User

- **Endpoint**: `/create_user`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - `200 OK`: User created successfully
  - `400 Bad Request`: User already exists

### Login

- **Endpoint**: `/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - `200 OK`: Login successful
  - `400 Bad Request`: Incorrect password
  - `404 Not Found`: User not found

## Running the Service

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install fastapi uvicorn pydantic
    ```

### Running the Server

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The service will be accessible at `http://127.0.0.1:8000`.

## Example Requests

### Create User

To create a new user, send a `POST` request to `/createuser`:

```bash
curl -X POST "http://127.0.0.1:8000/createuser" -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}'
```

### Login

To login, send a `POST` request to `/login`:

```bash
curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}'
```

## Project Structure

```
.
├── app.py        # The main FastAPI application
└── README.md      # This README file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [levitesn@oregonstate.edu].
