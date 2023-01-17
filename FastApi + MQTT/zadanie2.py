from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

filename ="plik.json"



# records = {
#     1: {
#         "temperature": 36,
#         "blood_pressure": 1000,
#         "time_of_sleep": 8

#     },
#     2: {
#         "temperature": 38,
#         "blood_pressure": 1100,
#         "time_of_sleep": 9

#     }
# }
# data_inicial = {
#     1: {
#          "temperature": 36,
#          "blood_pressure": 1000,
#          "time_of_sleep": 8
#     }
# }
# with open(filename,"w") as file2:
#     json.dump(data_inicial,file2)

            
class Record(BaseModel):
    temperature: int
    blood_pressure: int
    time_of_sleep: int


@app.get("/device")
def informations_about_device():
    return {"message" : "Smartwatch v. 1.0.0"}

@app.get("/records/{record_id}")
def device_record(record_id: int):
    with open(filename,"r") as file:
        data =json.load(file)
        print(data)
        print(data.get(str(record_id)))
    return {'record': data.get(str(record_id)) }

@app.get("/records")
def all_device_records():
    with open(filename,"r") as file:
        data =json.load(file)
    return {'records': data}

def merge_two_dicts(x, y):
    return {**x, **y}
    
@app.post("/add-record/{record_id}")
def create_record(record_id: int, record: Record):
    with open(filename,"r") as file:
         data_first =json.load(file)

    print(data_first)

    data = {record_id :{"temperature": record.temperature, "blood_pressure": record.blood_pressure, "time_of_sleep": record.time_of_sleep}}
    print(data)
    data_all = merge_two_dicts(data_first,data)
    print(data_all)
    with open(filename,"w") as file2:
        json.dump(data_all,file2)
    return data



@app.post("/change-record/{record_id}")
def change_record(record_id: int, record: Record):
    with open(filename,"r") as file:
         data_first =json.load(file)

    print(data_first)

    data = {record_id :{"temperature": record.temperature, "blood_pressure": record.blood_pressure, "time_of_sleep": record.time_of_sleep}}
    print(data)
    data_all = merge_two_dicts(data_first,data)
    print(data_all)
    with open(filename,"w") as file2:
        json.dump(data_all,file2)
    return data
    