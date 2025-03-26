import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("guestbook.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        message TEXT NOT NULL
    )
""")
conn.commit()

def save_message():
    name = name_entry.get()
    message = message_entry.get("1.0", tk.END).strip()

    if name and message:
        cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        messagebox.showinfo("Sparat!", "Ditt meddelande har sparats.")
        name_entry.delete(0, tk.END)
        message_entry.delete("1.0", tk.END)
        load_messages()
    else:
        messagebox.showwarning("Fel", "Både namn och meddelande måste fyllas i.")

def load_messages():
    messages_list.delete(0, tk.END)
    cursor.execute("SELECT name, message FROM messages ORDER BY id DESC")
    for row in cursor.fetchall():
        messages_list.insert(tk.END, f"{row[0]}: {row[1]}")

root = tk.Tk()
root.title("Gästbok")

tk.Label(root, text="Namn:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Meddelande:").pack()
message_entry = tk.Text(root, width=50, height=5)
message_entry.pack()

tk.Button(root, text="Spara", command=save_message).pack()

tk.Label(root, text="Gästboksinlägg:").pack()
messages_list = tk.Listbox(root, width=60, height=10)
messages_list.pack()

load_messages()

root.mainloop()

conn.close()
#test
print("HELLO WORLD")