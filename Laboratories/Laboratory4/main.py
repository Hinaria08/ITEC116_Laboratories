from fastapi import FastAPI, HTTPException, Request, Query, Depends
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

# Secret API Key
SECRET_KEY = os.getenv("API_NOCLUE")

def authenticate_request(api_key: str = Query(None, description="API Key required")):
    if not api_key or api_key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# Sample Task Data
tasks_version1 = [
    {"id": 1, "title": "Test 1", "description": "Complete FastAPI basics", "completed": False}
]

tasks_version2 = [
    {"id": 1, "title": "Test 2", "description": "Revise To-Do API", "completed": False}
]

# API v1 Routes
@app.get("/v1/tasks/{id}")
def fetch_task_v1(id: int, api_key: str = Depends(authenticate_request)):
    task = next((item for item in tasks_version1 if item["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return {"status": "success", "data": task}

@app.post("/v1/tasks/", status_code=201)
def add_task_v1(title: str, description: str, api_key: str = Depends(authenticate_request)):
    new_task = {"id": len(tasks_version1) + 1, "title": title, "description": description, "completed": False}
    tasks_version1.append(new_task)
    return {"status": "success", "data": new_task}

@app.delete("/v1/tasks/{id}", status_code=204)
def remove_task_v1(id: int, api_key: str = Depends(authenticate_request)):
    task = next((item for item in tasks_version1 if item["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_version1.remove(task)
    return {"status": "success", "message": "Task removed"}

@app.patch("/v1/tasks/{id}")
def modify_task_v1(id: int, title: str = None, description: str = None, completed: bool = None, api_key: str = Depends(authenticate_request)):
    task = next((item for item in tasks_version1 if item["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if title:
        task["title"] = title
    if description:
        task["description"] = description
    if completed is not None:
        task["completed"] = completed
    return {"status": "success", "data": task}

# API v2 Routes
@app.get("/v2/tasks/{id}")
def fetch_task_v2(id: int, api_key: str = Depends(authenticate_request)):
    task = next((item for item in tasks_version2 if item["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return {"status": "success", "data": task}

@app.post("/v2/tasks/", status_code=201)
def add_task_v2(title: str, description: str, api_key: str = Depends(authenticate_request)):
    new_task = {"id": len(tasks_version2) + 1, "title": title, "description": description, "completed": False}
    tasks_version2.append(new_task)
    return {"status": "success", "data": new_task}

@app.delete("/v2/tasks/{id}", status_code=204)
def remove_task_v2(id: int, api_key: str = Depends(authenticate_request)):
    task = next((item for item in tasks_version2 if item["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_version2.remove(task)
    return {"status": "success", "message": "Task removed"}

@app.patch("/v2/tasks/{id}")
def modify_task_v2(id: int, title: str = None, description: str = None, completed: bool = None, api_key: str = Depends(authenticate_request)):
    task = next((item for item in tasks_version2 if item["id"] == id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if title:
        task["title"] = title
    if description:
        task["description"] = description
    if completed is not None:
        task["completed"] = completed
    return {"status": "success", "data": task}

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the API. You can access versioned endpoints by using /v1/tasks/1 or /v2/tasks/1."}

@app.get("/health")
def health_check():
    return {"status": "API is healthy"}
