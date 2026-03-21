import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

# ------------------ BACKEND CLASSES ------------------

class Train:
    def __init__(self, train_no, source, destination, seats):
        self.train_no = train_no
        self.source = source
        self.destination = destination
        self.seats = seats
        self.waiting_list = []

    def book_ticket(self):
        pnr = random.randint(100000, 999999)
        if self.seats > 0:
            self.seats -= 1
            return pnr, "CONFIRMED"
        else:
            self.waiting_list.append(pnr)
            return pnr, "WAITING"


class Passenger:
    def __init__(self, name, age, gender, phone, status):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.status = status
        self.berth = random.choice(
            ["Lower", "Middle", "Upper"]) if status == "CONFIRMED" else "Not Allocated"


# ------------------ GUI APPLICATION ------------------

class RailwayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Railway Ticket Booking System")
        self.root.geometry("650x650")
        self.root.configure(bg="#E3F2FD")

        self.trains = [
            Train("12737", "Tadepalligudem", "Secunderabad", 2),
            Train("12728", "Tadepalligudem", "Visakhapatnam", 1)
        ]

        self.create_login_screen()

    # ---------------- LOGIN SCREEN ----------------
    def create_login_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#E3F2FD")
        frame.pack(pady=80)

        tk.Label(
            frame,
            text="Railway Ticket Booking",
            font=("Arial", 22, "bold"),
            bg="#E3F2FD",
            fg="#0D47A1"
        ).pack(pady=20)

        tk.Label(frame, text="Username", bg="#E3F2FD").pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(frame, text="Password", bg="#E3F2FD").pack()
        self.password_entry = tk.Entry(frame, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(
            frame,
            text="LOGIN",
            bg="#1976D2",
            fg="white",
            font=("Arial", 11, "bold"),
            width=15,
            command=self.login
        ).pack(pady=15)

    def login(self):
        if self.username_entry.get() and self.password_entry.get():
            self.create_booking_screen()
        else:
            messagebox.showerror("Error", "Enter username & password")

    # ---------------- BOOKING SCREEN ----------------
    def create_booking_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#E3F2FD")
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Ticket Booking",
            font=("Arial", 18, "bold"),
            bg="#E3F2FD",
            fg="#0D47A1"
        ).pack(pady=10)

        self.create_entry(frame, "Journey Date (DD-MM-YYYY)")
        self.date_entry = self.entry

        self.create_entry(frame, "Journey Time (HH:MM)")
        self.time_entry = self.entry

        tk.Label(frame, text="Select Train", bg="#E3F2FD").pack()
        self.train_var = tk.StringVar()
        self.train_menu = tk.OptionMenu(
            frame, self.train_var,
            *[f"{t.train_no} - {t.source} to {t.destination}" for t in self.trains]
        )
        self.train_menu.config(width=30)
        self.train_menu.pack(pady=5)

        self.create_entry(frame, "Passenger Name")
        self.name_entry = self.entry

        self.create_entry(frame, "Age")
        self.age_entry = self.entry

        self.create_entry(frame, "Gender")
        self.gender_entry = self.entry

        self.create_entry(frame, "Phone Number")
        self.phone_entry = self.entry

        tk.Button(
            frame,
            text="BOOK TICKET",
            bg="#2E7D32",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
            command=self.book_ticket
        ).pack(pady=15)

        self.output = tk.Text(frame, height=12, width=65)
        self.output.pack(pady=10)

    def create_entry(self, parent, label):
        tk.Label(parent, text=label, bg="#E3F2FD").pack()
        self.entry = tk.Entry(parent, width=35)
        self.entry.pack(pady=4)

    # ---------------- BOOK TICKET LOGIC ----------------
    def book_ticket(self):
        try:
            train_index = self.train_menu["menu"].index(self.train_var.get())
            train = self.trains[train_index]

            pnr, status = train.book_ticket()

            passenger = Passenger(
                self.name_entry.get(),
                int(self.age_entry.get()),
                self.gender_entry.get(),
                self.phone_entry.get(),
                status
            )

            self.display_ticket(train, passenger, pnr, status)
            self.save_to_file(train, passenger, pnr, status)

        except Exception as e:
            messagebox.showerror("Error", "Please fill all fields correctly")

    # ---------------- DISPLAY ----------------
    def display_ticket(self, train, passenger, pnr, status):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"PNR: {pnr}\n")
        self.output.insert(tk.END, f"Train: {train.train_no}\n")
        self.output.insert(tk.END, f"From: {train.source}\n")
        self.output.insert(tk.END, f"To: {train.destination}\n")
        self.output.insert(tk.END, f"Journey Date: {self.date_entry.get()}\n")
        self.output.insert(tk.END, f"Journey Time: {self.time_entry.get()}\n")
        self.output.insert(tk.END, f"Passenger: {passenger.name}\n")
        self.output.insert(tk.END, f"Status: {status}\n")
        self.output.insert(tk.END, f"Berth: {passenger.berth}\n")

    # ---------------- FILE STORAGE ----------------
    def save_to_file(self, train, passenger, pnr, status):
        with open("booked_tickets.txt", "a") as file:
            file.write("\n-------------------------------\n")
            file.write(f"PNR: {pnr}\n")
            file.write(f"Train: {train.train_no}\n")
            file.write(f"From: {train.source}\n")
            file.write(f"To: {train.destination}\n")
            file.write(f"Journey Date: {self.date_entry.get()}\n")
            file.write(f"Journey Time: {self.time_entry.get()}\n")
            file.write(f"Passenger Name: {passenger.name}\n")
            file.write(f"Age: {passenger.age}\n")
            file.write(f"Gender: {passenger.gender}\n")
            file.write(f"Phone: {passenger.phone}\n")
            file.write(f"Status: {status}\n")
            file.write(f"Berth: {passenger.berth}\n")
            file.write(f"Booked On: {datetime.now()}\n")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ------------------ MAIN ------------------

root = tk.Tk()
app = RailwayApp(root)
root.mainloop()
