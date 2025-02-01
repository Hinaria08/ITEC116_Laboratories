# FastAPI Development Labs

This repository contains five activities showcasing the implementation of API development using FastAPI. Each folder corresponds to a specific lab activity, focusing on different aspects of API development, from basic functionality to authentication and versioning.

## Laboratories

### 1. Factorial API

**Overview:**
This lab involved creating a simple API that calculates the factorial of a given number using FastAPI.

- Implemented a function to compute the factorial using a loop.
- **Endpoint:** `/factorial/{number}`
- If the input was `0`, the API returned `{ "result": false }`.
- Learned how to handle dynamic URL parameters in FastAPI.

### 2. To-Do List API

**Overview:**
This activity focused on implementing CRUD operations in an API. It introduced HTTP methods such as GET, POST, PATCH, and DELETE while ensuring proper request handling.

- Implemented a dictionary-based task management system.
- **Endpoints:**
  - `GET /tasks/{task_id}` → Retrieve a specific task.
  - `POST /tasks` → Add a new task.
  - `PATCH /tasks/{task_id}` → Update a task.
  - `DELETE /tasks/{task_id}` → Remove a task.
- Practiced request validation, response formatting, and HTTP method handling.

### 3. JSON Handling API

**Overview:**
This lab focused on JSON parsing and handling within an API. The goal was to retrieve user posts along with related comments and format structured responses.

- Implemented an API to fetch posts by a specific user.
- **Endpoint:** `GET /detailed_post/{userID}`
- Retrieved posts and their corresponding comments.
- Learned how to handle nested JSON structures effectively.

### 4. API Versioning & Authentication

**Overview:**
This lab introduced API versioning, authentication, and error handling to enhance security and maintainability.

- Implemented API versioning for different versions of the same endpoint.
- Added API key-based authentication using a `.env` file.
- **Error Responses:**
  - `404 Not Found` → When a requested task does not exist.
  - `201 Created` → When a new task was successfully added.
  - `204 No Content` → When a task was successfully updated or deleted.
- Learned best practices for securing API endpoints and handling errors effectively.

### 5. API Deployment

**Overview:**
This lab focused on deploying our API to a cloud platform (Render) and ensuring it functions correctly in a live environment.

- Successfully deployed Lab 4 API to Render.
- Used API key authentication for security.
- **Deployed Output:**
  - Hosted API at `itec116_<surname>.onrender.com`.
  - Configured API key authentication to match the environment variables used in the code.

## Setup

1. Install dependencies:
   ```sh
   pip install fastapi uvicorn python-dotenv
   ```
2. Navigate to the activity folder.
3. Run the server:
   ```sh
   uvicorn main:app --reload
   ```
4. API documentation available at:
   - [Swagger UI](http://127.0.0.1:8000/docs)

