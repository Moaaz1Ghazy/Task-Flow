
appointments = []

def book_appointment():
    patient = entry_app_patient.get()
    doctor = entry_app_doctor.get()

    if patient in patients and doctor in doctors:

        appointments.append((patient, doctor))

        messagebox.showinfo("Success", "Appointment Booked")

        entry_app_patient.delete(0, tk.END)
        entry_app_doctor.delete(0, tk.END)

    else:
        messagebox.showwarning("Error", "Invalid patient or doctor")


def show_appointments():

    if appointments:

        text = ""

        for app in appointments:
            text += f"{app[0]} -> {app[1]}\n"

    else:
        text = "No appointments"

    messagebox.showinfo("Appointments", text)
window = tk.Tk()

window.title("Hospital Management System")

window.geometry("450x600")

window.configure(bg="lightblue")

title = tk.Label(
    window,
    text="Hospital System",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)

title.pack(pady=10)

# Patients UI
tk.Label(window, text="Patient Name", bg="lightblue").pack()

entry_patient = tk.Entry(window)
entry_patient.pack()

tk.Button(window, text="Add Patient", command=add_patient).pack()

tk.Button(window, text="Delete Patient", command=delete_patient).pack()

tk.Button(window, text="Search Patient", command=search_patient).pack()


# Doctors UI
tk.Label(window, text="\nDoctor Name", bg="lightblue").pack()

entry_doctor = tk.Entry(window)
entry_doctor.pack()

tk.Button(window, text="Add Doctor", command=add_doctor).pack()

tk.Button(window, text="Search Doctor", command=search_doctor).pack()


# Appointment UI
tk.Label(window, text="\nAppointment Patient", bg="lightblue").pack()

entry_app_patient = tk.Entry(window)
entry_app_patient.pack()

tk.Label(window, text="Appointment Doctor", bg="lightblue").pack()

entry_app_doctor = tk.Entry(window)
entry_app_doctor.pack()

tk.Button(window, text="Book Appointment", command=book_appointment).pack()

tk.Button(window, text="Show Appointments", command=show_appointments).pack()
