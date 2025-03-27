import tkinter as tk
from tkcalendar import Calendar
from data.appointment_service import add_appointment

def open_appointment_form():
    window = tk.Toplevel()
    window.title("Add Appointment")

    tk.Label(window, text="Patient ID").pack()
    patient_id = tk.Entry(window)
    patient_id.pack()

    tk.Label(window, text="Doctor ID").pack()
    doctor_id = tk.Entry(window)
    doctor_id.pack()

    tk.Label(window, text="Appointment Date").pack()
    cal = Calendar(window)
    cal.pack()

    tk.Label(window, text="Reason").pack()
    reason = tk.Entry(window)
    reason.pack()

    def submit():
        add_appointment(patient_id.get(), doctor_id.get(), cal.get_date(), reason.get())
        window.destroy()

    tk.Button(window, text="Submit", command=submit).pack()
