import sqlite3
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Get the directory where the py script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the SQLite database file
db_file = os.path.join(script_dir, "inventory.db")

if not os.path.exists(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY,
                   Name TEXT,
                   Price REAL,
                   Quantity INTEGER
                   )''')

    conn.commit()
    conn.close()

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Inventory")
        self.resizable(False, False)
        self.config(bg="#A79277")

        self.create_widgets()

    def create_widgets(self):
        # Btn
        btn_add = tk.Button(self, text="Add", font=("Arial", 18), width=10, command=self.add_entry_window)
        btn_remove = tk.Button(self, text="Remove", font=("Arial", 18), width=10, command=self.remove_entry_window)
        btn_update = tk.Button(self, text="Update", font=("Arial", 18), width=10, command=self.update_entry_window)
        btn_view = tk.Button(self, text="View", font=("Arial", 18), width=10, command=self.view_entry)
        btn_exit = tk.Button(self, text="Exit", font=("Arial", 11), width=8, command=self.exit_program)

        # Btn Pos
        btn_add.place(x=80, y=350)
        btn_remove.place(x=240, y=350)
        btn_update.place(x=80, y=410)
        btn_view.place(x=240, y=410)
        btn_exit.place(x=410, y=460)

        # Frame
        self.frame = tk.Frame(self, width=480, height=300, bg="#EAD8C0")
        self.frame.place(x=10, y=10)

        #TreeView
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Name", "Price", "Quantity"), show="headings", height=10, style="Custom.Treeview")
        self.tree.column(0, anchor="center", stretch=False, width=110)
        self.tree.column(1, anchor="center", stretch=False, width=120)
        self.tree.column(2, anchor="center", stretch=False, width=120)
        self.tree.column(3, anchor="center", stretch=False, width=120)
        self.tree.heading(0, text="ID")
        self.tree.heading(1, text="Name")
        self.tree.heading(2, text="Price")
        self.tree.heading(3, text="Quantity")
        self.tree.pack(side="left")

        # Config Style For TreeView
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading", font=("Arial", 17))
        style.configure("Custom.Treeview", font=("Arial", 16), background="#EADBC8", fieldbackground="#EADBC8")
        style.configure("Custom.Treeview", rowheight=28)

        # TreeView Scroll
        self.tree.bind('<Button-1>', 'break')
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
    
    # Add
    def add_entry_window(self):
        self.add_window = tk.Toplevel(self)
        self.add_window.title("Add")
        self.add_window.geometry("300x300")
        self.add_window.config(bg="#A79277")
        self.add_window.resizable(False, False)

        # Frame
        self.add_frame = tk.Frame(self.add_window, width=280, height=280 , bg="#EAD8C0")
        self.add_frame.place(x=10, y=10)

        # lbl
        lbl_name_add = tk.Label(self.add_frame, text="Name:", font=("Arial", 18, "bold"), bg="#EAD8C0")
        lbl_price_add = tk.Label(self.add_frame, text="Price:", font=("Arial", 18, "bold"), bg="#EAD8C0")
        lbl_quantity_add = tk.Label(self.add_frame, text="Quantity:", font=("Arial", 18, "bold"), bg="#EAD8C0")

        # lbl Pos
        lbl_name_add.place(x=10, y=20)
        lbl_price_add.place(x=10, y=60)
        lbl_quantity_add.place(x=10, y=100)

        # Ent
        self.ent_name_add = tk.Entry(self.add_frame, font=("Arial", 14, "bold"), width=15)
        self.ent_price_add = tk.Entry(self.add_frame, font=("Arial", 14, "bold"), width=15)
        self.ent_quantity_add = tk.Entry(self.add_frame, font=("Arial", 14, "bold"), width=12)

        # Ent pos
        self.ent_name_add.place(x=90, y=24)
        self.ent_price_add.place(x=90, y=64)
        self.ent_quantity_add.place(x=120, y=104)

        # Btn
        btn_add = tk.Button(self.add_frame, text="Add", font=("Arial", 16, "bold"), width=10, command=self.add_entry)
        btn_cancel_add = tk.Button(self.add_frame, text="Cancel", font=("Arial", 16, "bold"), width=6, command=lambda: self.add_window.destroy())

        # Btn Pos
        btn_add.place(x=70, y=180)
        btn_cancel_add.place(x=95, y=230)

    # Remove
    def remove_entry_window(self):
        self.remove_window = tk.Toplevel(self)
        self.remove_window.title("Add")
        self.remove_window.geometry("300x300")
        self.remove_window.config(bg="#A79277")
        self.remove_window.resizable(False, False)

        # Frame
        self.remove_frame = tk.Frame(self.remove_window, width=280, height=280 , bg="#EAD8C0")
        
        # lbl
        lbl_id_remove = tk.Label(self.remove_frame, text="ID:", font=("Arial", 18, "bold"), bg="#EAD8C0")

        # Ent
        self.ent_id_remove = tk.Entry(self.remove_frame, font=("Arial", 14, "bold"), width=15)

        # Btn
        btn_remove = tk.Button(self.remove_frame, text="Remove", font=("Arial", 16, "bold"), width=10, command=self.remove_entry)
        btn_cancel_remove = tk.Button(self.remove_frame, text="Cancel", font=("Arial", 16, "bold"), width=6, command=lambda: self.remove_window.destroy())

        # Pos
        self.remove_frame.place(x=10, y=10)
        lbl_id_remove.place(x=30, y=60)
        self.ent_id_remove.place(x=90, y=64)
        btn_remove.place(x=70, y=180)
        btn_cancel_remove.place(x=95, y=230)

    # Update
    def update_entry_window(self):
        self.update_window = tk.Toplevel(self)
        self.update_window.title("Add")
        self.update_window.geometry("300x300")
        self.update_window.config(bg="#A79277")
        self.update_window.resizable(False, False)

        # Frame
        self.update_frame = tk.Frame(self.update_window, width=280, height=280 , bg="#EAD8C0")
        self.update_frame.place(x=10, y=10)

        # lbl
        lbl_id_update = tk.Label(self.update_frame, text="ID:", font=("Arial", 18, "bold"), bg="#EAD8C0")
        lbl_name_update = tk.Label(self.update_frame, text="Name:", font=("Arial", 18, "bold"), bg="#EAD8C0")
        lbl_price_update = tk.Label(self.update_frame, text="Price:", font=("Arial", 18, "bold"), bg="#EAD8C0")
        lbl_quantity_update = tk.Label(self.update_frame, text="Quantity:", font=("Arial", 18, "bold"), bg="#EAD8C0")

        # lbl Pos
        lbl_id_update.place(x=10, y=20)
        lbl_name_update.place(x=10, y=50)
        lbl_price_update.place(x=10, y=80)
        lbl_quantity_update.place(x=10, y=110)

        # Ent
        self.ent_id_update = tk.Entry(self.update_frame, font=("Arial", 14, "bold"), width=19)
        self.ent_name_update = tk.Entry(self.update_frame, font=("Arial", 14, "bold"), width=15)
        self.ent_price_update = tk.Entry(self.update_frame, font=("Arial", 14, "bold"), width=15)
        self.ent_quantity_update = tk.Entry(self.update_frame, font=("Arial", 14, "bold"), width=12)

        # Ent pos
        self.ent_id_update.place(x=50, y=23)
        self.ent_name_update.place(x=90, y=53)
        self.ent_price_update.place(x=90, y=83)
        self.ent_quantity_update.place(x=120, y=113)

        # Btn
        btn_update = tk.Button(self.update_frame, text="Update", font=("Arial", 16, "bold"), width=10, command=self.update_entry)
        btn_cancel_update = tk.Button(self.update_frame, text="Cancel", font=("Arial", 16, "bold"), width=6, command=lambda: self.update_window.destroy())

        # Btn Pos
        btn_update.place(x=70, y=180)
        btn_cancel_update.place(x=95, y=230)

    # Window Functions
    # Add Data Entries into DB
    def add_entry(self):
        name = self.ent_name_add.get()
        price = self.ent_price_add.get()
        quantity = self.ent_quantity_add.get()

        if name and price and quantity:
            if price.isalpha() and quantity.isalpha():
                messagebox.showerror("Oops", "Invalid price or quantity")
            else:
                conn = sqlite3.connect(db_file)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO products (Name, Price, Quantity) VALUES(?, ?, ?)", (name, price, quantity))
                conn.commit()
                conn.close()  
                self.add_window.destroy()         
        else:
            messagebox.showerror("Oops", "Please fill out the fields")
        
    # Remove Data Entries in DB
    def remove_entry(self):
        entered_id = self.ent_id_remove.get()
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM products WHERE id=?", (entered_id,))
        table_id = cursor.fetchone()
        
        if table_id is not None and table_id[0] == int(entered_id):
            cursor.execute("DELETE FROM products WHERE id=?", (entered_id,))
            conn.commit()
            conn.close()
            self.remove_window.destroy()
        else:
            messagebox.showerror("Oops", "Id does not exist")

    # Update Data Entrires in DB
    def update_entry(self):
        entered_id = self.ent_id_update.get()
        name = self.ent_name_update.get()
        price = self.ent_price_update.get()
        quantity = self.ent_quantity_update.get()

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM products WHERE id=?", (entered_id,))
        fetched_id = cursor.fetchone()

        if fetched_id is not None and entered_id and name and price and quantity:
            if name.isalpha() and price.isdigit() and quantity.isdigit():

                if int(entered_id) == fetched_id[0]:
                    cursor.execute("UPDATE products SET Name=? WHERE id=?", (name, entered_id))
                    cursor.execute("UPDATE products SET Price=? WHERE id=?", (price, entered_id))
                    cursor.execute("UPDATE products SET Quantity=? WHERE id=?", (quantity, entered_id))
                    conn.commit()
                    conn.close()
                    self.update_window.destroy()

                    self.view_entry()
                else:
                    messagebox.showerror("Oops", "Id does not exist")
            else:
                messagebox.showerror("Oops", "Invalid Values")
        else:
            messagebox.showerror("Oops", "Please out all the fields or Id does not exist")
        
    # Insert Entries to TreeView
    def view_entry(self):
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        entries = cursor.fetchall()
        conn.close()

        for record in self.tree.get_children():
            self.tree.delete(record)

        if entries:
            for rows in entries:
                price = rows[2]

                formatted_price = "₱{:.2f}".format(abs(price))
                formatted_entry = (rows[0], rows[1], formatted_price, rows[3])

                self.tree.insert("", 'end', values=formatted_entry)
    # Exit Program            
    def exit_program(self):
        self.destroy()

win = Window()
win.mainloop()
