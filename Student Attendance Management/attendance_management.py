import csv
from pathlib import Path
from datetime import date
import tkinter as tk
from tkinter import ttk, messagebox

FILE = Path(__file__).with_name("attendance.csv")

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        root.title("Attendance Management")
        root.geometry("700x480")
        ttk.Label(root, text="Attendance Management System", font=("Arial", 18, "bold")).pack(pady=12)
        form = ttk.Frame(root)
        form.pack(fill="x", padx=12, pady=8)
        self.student = tk.StringVar()
        ttk.Label(form, text="Student name").pack(side="left", padx=5)
        ttk.Entry(form, textvariable=self.student, width=28).pack(side="left", padx=5)
        ttk.Button(form, text="Mark Present", command=lambda: self.mark("Present")).pack(side="left", padx=5)
        ttk.Button(form, text="Mark Absent", command=lambda: self.mark("Absent")).pack(side="left", padx=5)
        ttk.Button(form, text="Refresh", command=self.load).pack(side="left", padx=5)

        self.table = ttk.Treeview(root, columns=("date", "student", "status"), show="headings")
        for col, title, width in [("date", "Date", 160), ("student", "Student", 330), ("status", "Status", 160)]:
            self.table.heading(col, text=title)
            self.table.column(col, width=width)
        self.table.pack(fill="both", expand=True, padx=12, pady=10)
        self.load()

    def mark(self, status):
        name = self.student.get().strip()
        if not name:
            messagebox.showwarning("Missing name", "Enter the student's name.")
            return
        new_file = not FILE.exists()
        with FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow(["date", "student", "status"])
            writer.writerow([date.today().isoformat(), name, status])
        self.student.set("")
        self.load()

    def load(self):
        for item in self.table.get_children():
            self.table.delete(item)
        if FILE.exists():
            with FILE.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    self.table.insert("", "end", values=(row.get("date", ""), row.get("student", ""), row.get("status", "")))

root = tk.Tk()
AttendanceApp(root)
root.mainloop()
