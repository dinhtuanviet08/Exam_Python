from data.db import db

doctors_collection = db["doctors"]

def add_doctor(full_name, specialization, phone, email, experience):
    doctor = {
        "full_name": full_name,
        "specialization": specialization,
        "phone": phone,
        "email": email,
        "experience": experience
    }
    return doctors_collection.insert_one(doctor).inserted_id

def get_all_doctors():
    return list(doctors_collection.find({}))

def get_doctor_by_id(doctor_id):
    return doctors_collection.find_one({"_id": doctor_id})
