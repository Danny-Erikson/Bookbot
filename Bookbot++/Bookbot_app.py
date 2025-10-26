# Used for GUI
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, font


class BookBotApp:
    def __init__(self, master):
        # *Initialization tkinter
        self.master = master
        master.title("Bookbot++")
        master.geometry("500x300")

        # State variables
        self.file_path = None

        # *Create UI elements
        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        """Create UI elements."""
        bold_font = font.Font(weight="bold")
        self.file_select = ttk.Button(
            self.master, text="Select a File", command=self.select_file)
        self.file_label = ttk.Label(
            self.master, text="Selected file:", font=bold_font)
        self.file = ttk.Label(self.master)

    def _layout_widgets(self):
        """Pack/place/grid UI elements."""
        self.file_select.pack(side=tk.TOP, pady=20)
        self.file_label.pack(side=tk.LEFT, padx=(10, 2))
        self.file.pack(side=tk.LEFT, padx=(2, 10))

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path = path
            file_name = path.split("/")[-1]
            self.file.config(text=file_name)
