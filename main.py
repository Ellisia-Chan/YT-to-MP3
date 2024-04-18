import tkinter as tk
from tkinter import filedialog
import pytube as pt
import os

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube to MP3 Converter")
        self.geometry("500x500")
        self.resizable(False, False)
        self.config(bg="#F3D0D7")

        self.Create_Widgets()

    def Create_Widgets(self):
        #Frame
        frame = tk.Frame(self, width=480, height=480, bd=3, relief=tk.GROOVE, bg="#FFEFEF")
        frame.place(x=10, y=10)

        #Lbl
        lbl_Title = tk.Label(frame, text="Youtube to MP3 Converter", font=("Arial", 24), bg="#FFEFEF")
        lbl_Title.place(x=50, y=10)

        lbl_Link_title = tk.Label(frame, text="Link:", font=("Arial", 16), bg="#FFEFEF")
        lbl_Link_title.place(x=50, y=80)

        lbl_filePath_title = tk.Label(frame, text="Filepath:", font=("Arial", 16), bg="#FFEFEF")
        lbl_filePath_title.place(x=50, y=150)

        #Ent
        self.ent_link = tk.Entry(frame, width=30, bd=2, font=("Arial", 16))
        self.ent_link.place(x=50, y=110)

        self.ent_filepath = tk.Entry(frame, width=32, bd=2, font=("Arial", 11))
        self.ent_filepath.place(x=50, y=180)

        #Btn
        self.btn_select_filepath = tk.Button(frame, text="Select Path", font=("Arial", 11))
        self.btn_select_filepath.place(x=320, y=175)

        self.btn_convert = tk.Button(frame, text="Convert", font=("Arial", 16), width=12)
        self.btn_convert.place(x=150, y=220)

        
        



win = Window()

win.mainloop()