from fastapi import FastAPI
import json
app = FastAPI()  #object of FastAPI class

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data


@app.get("/")  #endpoint, decorator to define a GET request at the root URL 

def hello():
    return {"message": "Patient management sys API"}  #response in JSON format

@app.get("/about")
def about():
    return {'message': 'A fully funcional API for patient management system'}  #response in JSON format


@app.get('/view')  #endpoint to load all the data
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')  #routing syntax
def view_patient(patient_id: str):
    #load all the patients
    data = load_data()

    if(patient_id in data):
        return data[patient_id]
    return {'error':'patient not found'}


