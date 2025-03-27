import tkinter as tk
from data.patient_service import add_patient

def open_patient_form():
    window = tk.Toplevel()
    window.title("Add Patient")

    tk.Label(window, text="Full Name").pack()
    full_name = tk.Entry(window)
    full_name.pack()

    tk.Label(window, text="Date of Birth").pack()
    dob = tk.Entry(window)
    dob.pack()

    tk.Label(window, text="Gender").pack()
    gender = tk.Entry(window)
    gender.pack()

    tk.Label(window, text="Address").pack()
    address = tk.Entry(window)
    address.pack()

    tk.Label(window, text="Phone").pack()
    phone = tk.Entry(window)
    phone.pack()

    tk.Label(window, text="Email").pack()
    email = tk.Entry(window)
    email.pack()

    def submit():
        add_patient(full_name.get(), dob.get(), gender.get(), address.get(), phone.get(), email.get())
        window.destroy()

    tk.Button(window, text="Submit", command=submit).pack()
