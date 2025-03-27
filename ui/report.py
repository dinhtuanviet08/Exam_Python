import tkinter as tk
from data.appointment_service import get_all_appointments

def open_report_form():
    window = tk.Toplevel()
    window.title("Appointment Report")

    tk.Label(window, text="Appointments Report", font=("Arial", 14)).pack(pady=10)

    appointments = get_all_appointments()

    for appt in appointments:
        info = f"Patient: {appt['patient_id']} | Doctor: {appt['doctor_id']} | Date: {appt['appointment_date']} | Status: {appt['status']}"
        tk.Label(window, text=info).pack()

    tk.Button(window, text="Close", command=window.destroy).pack(pady=10)
