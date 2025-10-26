# Used for GUI
import tkinter as tk
from tkinter import filedialog


class BookBotApp:
    def __init__(self, master):
        # Master will be root for tkinker
        self.master = master
        master.title("Bookbot++")
        master.geometry("500x300")

        # State for file path varable
        self.file_path = None

        self.file_select = tk.Button(
            master, text="Select a File", command=self.select_file)
        self.file_select.pack()

        self.file_label = tk.Label(master)
        self.file_label.pack()

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path = path
            self.file_label.config(text={path})
