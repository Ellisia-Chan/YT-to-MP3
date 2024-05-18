import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
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
        # Frame
        frame = tk.Frame(self, width=480, height=480, bd=3, relief=tk.GROOVE, bg="#FFEFEF")
        frame.place(x=10, y=10)

        # Labels
        lbl_Title = tk.Label(frame, text="Youtube to MP3 Converter", font=("Arial", 24), bg="#FFEFEF")
        lbl_Title.place(x=50, y=10)

        lbl_Link_title = tk.Label(frame, text="Link:", font=("Arial", 16), bg="#FFEFEF")
        lbl_Link_title.place(x=50, y=80)

        lbl_filePath_title = tk.Label(frame, text="Filepath:", font=("Arial", 16), bg="#FFEFEF")
        lbl_filePath_title.place(x=50, y=150)

        # Entry fields
        self.ent_link = tk.Entry(frame, width=40, bd=2, font=("Arial", 13))
        self.ent_link.place(x=50, y=110)

        self.ent_filepath = tk.Entry(frame, width=32, bd=2, font=("Arial", 11), state="readonly")
        self.ent_filepath.place(x=50, y=180)

        # Buttons
        self.btn_select_filepath = tk.Button(frame, text="Select Path", font=("Arial", 11), command=self.filepath)
        self.btn_select_filepath.place(x=320, y=175)

        self.btn_convert = tk.Button(frame, text="Convert", font=("Arial", 16), width=12, command=self.convert_link)
        self.btn_convert.place(x=150, y=260)
    
    def filepath(self):
        path = filedialog.askdirectory()
        print(path)
        if path:
            self.ent_filepath.config(state="normal")
            self.ent_filepath.delete(0, tk.END)
            self.ent_filepath.insert(tk.END, path)
            self.ent_filepath.config(state="readonly")
    
    def convert_link(self):
        link = self.ent_link.get()
        download_path = self.ent_filepath.get()

        if not link:
            messagebox.showerror("Error", "Please enter a YouTube link.")
            return
        
        if not download_path:
            messagebox.showerror("Error", "Please select a download path.")
            return

        try:
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()
            if not video:
                raise Exception("No audio stream found")
            
            out_file = video.download(output_path=download_path)
            print(f"Downloaded file path: {out_file}")

            # Save the file as .mp3
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
            messagebox.showinfo("Success", f"Downloaded and saved as {new_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            print(f"An error occurred: {e}")

# Initialize the window
win = Window()
win.mainloop()
