from datetime import datetime

class Appointment:
    def __init__(self, patient_id, doctor_id, appointment_date, reason, status="pending"):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M:%S")
        self.reason = reason
        self.status = status

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "appointment_date": self.appointment_date.strftime("%Y-%m-%d %H:%M:%S"),
            "reason": self.reason,
            "status": self.status
        }
