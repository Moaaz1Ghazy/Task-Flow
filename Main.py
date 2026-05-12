import tkinter as tk

FILE = "tasks.txt"

def save():
    with open(FILE, "w") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")

def load():
    try:
        with open(FILE, "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except:
        pass

def add():
    if entry.get():
        listbox.insert(tk.END, entry.get())
        entry.delete(0, tk.END)
        save()

def delete():
    if listbox.curselection():
        listbox.delete(listbox.curselection())
        save()

def edit():
    if listbox.curselection() and entry.get():
        i = listbox.curselection()[0]
        listbox.delete(i)
        listbox.insert(i, entry.get())
        entry.delete(0, tk.END)
        save()

# واجهة
root = tk.Tk()
root.title("ToDo")
root.geometry("300x400")

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Delete", command=delete).pack()
tk.Button(root, text="Edit", command=edit).pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

load()
root.mainloop()
