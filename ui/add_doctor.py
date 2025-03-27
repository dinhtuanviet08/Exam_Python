import tkinter as tk
from data.doctor_service import add_doctor

def open_doctor_form():
    window = tk.Toplevel()
    window.title("Add Doctor")

    tk.Label(window, text="Full Name").pack()
    full_name = tk.Entry(window)
    full_name.pack()

    tk.Label(window, text="Specialization").pack()
    specialization = tk.Entry(window)
    specialization.pack()

    tk.Label(window, text="Phone").pack()
    phone = tk.Entry(window)
    phone.pack()

    tk.Label(window, text="Email").pack()
    email = tk.Entry(window)
    email.pack()

    tk.Label(window, text="Experience (years)").pack()
    experience = tk.Entry(window)
    experience.pack()

    def submit():
        add_doctor(full_name.get(), specialization.get(), phone.get(), email.get(), int(experience.get()))
        window.destroy()

    tk.Button(window, text="Submit", command=submit).pack()
