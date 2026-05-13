import tkinter as tk
from tkinter import messagebox

patients_list = []

def handle_add():
    patient_name = entry_patient.get().strip()
    if patient_name:
        patients_list.append(patient_name)
        entry_patient.delete(0, tk.END)
        messagebox.showinfo("Success", f"Patient {patient_name} added")
    else:
        messagebox.showwarning("Warning", "Please enter a name")

def handle_delete():
    target_name = entry_patient.get().strip()
    if target_name in patients_list:
        patients_list.remove(target_name)
        entry_patient.delete(0, tk.END)
        messagebox.showinfo("Deleted", "Patient removed")
    else:
        messagebox.showerror("Error", "Name not found")
def handle_search():
    query_name = entry_patient.get().strip()
    if query_name in patients_list:
        messagebox.showinfo("Result", f"Yes, {query_name} is here")
    else:
        messagebox.showwarning("Result", "Name not found")
root = tk.Tk()
root.title("Patient Management System")
root.geometry("400x300")

entry_patient = tk.Entry(root, font=("Arial", 14))
entry_patient.pack(pady=20)

btn_add = tk.Button(root, text="Add Patient", command=handle_add, bg="green", fg="white")
btn_add.pack(fill="x", padx=50, pady=5)

btn_search = tk.Button(root, text="Search Patient", command=handle_search, bg="blue", fg="white")
btn_search.pack(fill="x", padx=50, pady=5)

btn_delete = tk.Button(root, text="Delete Patient", command=handle_delete, bg="red", fg="white")
btn_delete.pack(fill="x", padx=50, pady=5)
doctors = []

def add_doctor():
    name = entry_doctor.get()

    if name:
        doctors.append(name)

        entry_doctor.delete(0, tk.END)

        messagebox.showinfo("Success", "Doctor Added")


def search_doctor():
    name = entry_doctor.get()

    if name in doctors:
        messagebox.showinfo("Found", "Doctor exists")

    else:
        messagebox.showinfo("Result", "Doctor not found")
# Appointment UI
tk.Label(window, text="\nAppointment Patient", bg="lightblue").pack()

entry_app_patient = tk.Entry(window)
entry_app_patient.pack()

tk.Label(window, text="Appointment Doctor", bg="lightblue").pack()

entry_app_doctor = tk.Entry(window)
entry_app_doctor.pack()

tk.Button(window, text="Book Appointment", command=book_appointment).pack()

tk.Button(window, text="Show Appointments", command=show_appointments).pack()
Commit
git commit -m "GUI design created"
root.mainloop()
