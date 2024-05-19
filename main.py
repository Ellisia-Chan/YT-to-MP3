import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
import os
import threading

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube to MP3/MP4 Converter")
        self.geometry("500x500")
        self.resizable(False, False)
        self.config(bg="#F3D0D7")

        self.Create_Widgets()

    def Create_Widgets(self):
        # Frame
        frame = tk.Frame(self, width=480, height=480, bd=3, relief=tk.GROOVE, bg="#FFEFEF")
        frame.place(x=10, y=10)

        # Labels
        lbl_Title = tk.Label(frame, text="YouTube to MP3/MP4 Converter", font=("Arial", 20), bg="#FFEFEF")
        lbl_Title.place(x=40, y=10)

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

        self.btn_convert = tk.Button(frame, text="Convert", font=("Arial", 16), width=12, command=self.start_conversion)
        self.btn_convert.place(x=150, y=300)
        
        # RadioButton
        self.radio = tk.IntVar()
        rd_mp3 = tk.Radiobutton(frame, text="MP3", font=("Arial", 16), variable=self.radio, value=1)
        rd_mp4 = tk.Radiobutton(frame, text="MP4", font=("Arial", 16), variable=self.radio, value=2)
        
        rd_mp3.place(x=150, y=220)
        rd_mp4.place(x=230, y=220)

        # Progress bar
        self.progress = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
        self.progress.place(x=90, y=260)

    def filepath(self):
        path = filedialog.askdirectory()
        if path:
            self.ent_filepath.config(state="normal")
            self.ent_filepath.delete(0, tk.END)
            self.ent_filepath.insert(tk.END, path)
            self.ent_filepath.config(state="readonly")

    def start_conversion(self):
        threading.Thread(target=self.convert_link).start()

    def progress_function(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = (size - bytes_remaining) / size * 100
        self.progress['value'] = progress
        self.update_idletasks()

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
            radio_value = self.radio.get()
            file_format = None
            
            yt = YouTube(link, on_progress_callback=self.progress_function)
            
            if radio_value == 1:
                # Download audio stream for MP3
                file_format = '.mp3'
                stream = yt.streams.filter(only_audio=True).first()
                if not stream:
                    raise Exception("No audio stream found")
            elif radio_value == 2:
                # Download high-quality video stream for MP4
                file_format = '.mp4'
                stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                if not stream:
                    raise Exception("No video stream found")
            else:
                raise Exception("Select File Format")
            
            base = os.path.join(download_path, yt.title)
            new_file = base + file_format
            
            if os.path.exists(new_file):
                overwrite = messagebox.askyesno("File Exists", f"The file '{new_file}' already exists. Do you want to overwrite it?")
                if not overwrite:
                    # Generate a new file name
                    counter = 1
                    while os.path.exists(new_file):
                        new_file = f"{base}({counter}){file_format}"
                        counter += 1
            
            # Download and rename the file
            out_file = stream.download(output_path=download_path)
            os.rename(out_file, new_file)
            
            self.progress['value'] = 0  # Reset progress bar after download completes
            
            messagebox.showinfo("Success", f"Downloaded and saved as {new_file}")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")



# Initialize the window
win = Window()
win.mainloop()
