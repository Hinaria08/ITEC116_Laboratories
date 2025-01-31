from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

records = [{"id": 1, "name": "Lab Activity", "details": "Complete Lab 2", "status": False}]

class Record(BaseModel):
    name: str
    details: str
    status: bool = False

@app.get("/records/{record_id}")
def get_record(record_id: int):
    record = next((rec for rec in records if rec["id"] == record_id), None)
    if record:
        return {"success": True, "data": record}
    raise HTTPException(status_code=404, detail="Record not found")

@app.post("/records")
def create_record(record: Record):
    new_id = (max(rec["id"] for rec in records) + 1) if records else 1
    new_record = {"id": new_id, **record.dict()}
    records.append(new_record)
    return {"success": True, "data": new_record}

@app.patch("/records/{record_id}")
def update_record(record_id: int, record_data: Record):
    record = next((rec for rec in records if rec["id"] == record_id), None)
    if record:
        record.update(record_data.dict())
        return {"success": True, "data": record}
    raise HTTPException(status_code=404, detail="Record not found")

@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    record = next((rec for rec in records if rec["id"] == record_id), None)
    if record:
        records.remove(record)
        return {"success": True, "message": f"Record {record_id} deleted"}
    raise HTTPException(status_code=404, detail="Record not found")

@app.put("/records/{record_id}")
def replace_record(record_id: int, record: Record):
    index = next((i for i, rec in enumerate(records) if rec["id"] == record_id), None)
    if index is not None:
        updated_record = {"id": record_id, **record.dict()}
        records[index] = updated_record
        return {"success": True, "data": updated_record}
    raise HTTPException(status_code=404, detail="Record not found")
