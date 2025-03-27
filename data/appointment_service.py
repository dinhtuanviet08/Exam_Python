from data.db import db
from bson.objectid import ObjectId

appointments_collection = db["appointments"]

def add_appointment(patient_id, doctor_id, appointment_date, reason, status="pending"):
    appointment = {
        "patient_id": ObjectId(patient_id),
        "doctor_id": ObjectId(doctor_id),
        "appointment_date": appointment_date,
        "reason": reason,
        "status": status
    }
    return appointments_collection.insert_one(appointment).inserted_id

def get_all_appointments():
    return list(appointments_collection.find({}))

def get_appointments_today():
    from datetime import datetime
    today = datetime.today().strftime("%Y-%m-%d")
    return list(appointments_collection.find({"appointment_date": {"$regex": today}}))
