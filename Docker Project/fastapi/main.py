from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

records = {
    1: {
        "temperature": 36,
        "blood_pressure": 1000,
        "time_of_sleep": 8
        },
    2: {
        "temperature": 38,
        "blood_pressure": 1100,
        "time_of_sleep": 9
        }
    }

class Record(BaseModel):
    temperature: int
    blood_pressure: int
    time_of_sleep: int

@app.get("/device")
def informations_about_device():
    return {"message" : "Smartwatch v. 1.0.0"}

@app.get("/records")
def all_device_records():
    return {"records" : records}

@app.post("/add-record/{record_id}")
def create_record(record_id: int, record: Record):
    if record_id in records:
        return {"Record already exists"}
    else:
        records[record_id] = {"temperature": record.temperature, "blood_pressure": record.blood_pressure, "time_of_sleep": record.time_of_sleep}
        return records[record_id]