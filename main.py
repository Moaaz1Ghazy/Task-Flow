 Appointments Section
# =========================
# MEMBER 3 - APPOINTMENTS
# =========================

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
Commit
git commit -m "Appointments system added"