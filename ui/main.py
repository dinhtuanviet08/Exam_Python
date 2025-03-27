import tkinter as tk
from ui.add_patient import open_patient_form
from ui.add_doctor import open_doctor_form
from ui.add_appointment import open_appointment_form
from ui.report import open_report_form

def open_main_window():
    root = tk.Tk()
    root.title("Hospital Management System")

    tk.Button(root, text="Add Patient", command=open_patient_form).pack(pady=5)
    tk.Button(root, text="Add Doctor", command=open_doctor_form).pack(pady=5)
    tk.Button(root, text="Add Appointment", command=open_appointment_form).pack(pady=5)
    tk.Button(root, text="View Report", command=open_report_form).pack(pady=5)

    root.mainloop()
