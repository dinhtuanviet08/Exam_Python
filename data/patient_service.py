from data.db import db

patients_collection = db["patients"]

def add_patient(full_name, date_of_birth, gender, address, phone, email):
    patient = {
        "full_name": full_name,
        "date_of_birth": date_of_birth,
        "gender": gender,
        "address": address,
        "phone": phone,
        "email": email
    }
    return patients_collection.insert_one(patient).inserted_id

def get_all_patients():
    return list(patients_collection.find({}))

def get_patient_by_id(patient_id):
    return patients_collection.find_one({"_id": patient_id})
