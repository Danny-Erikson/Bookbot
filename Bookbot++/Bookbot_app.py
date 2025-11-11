# Used for GUI
import tkinter as tk
from tkinter import ttk, filedialog, font


class BookBotApp:
    def __init__(self, master):
        # *Initialization tkinter
        self.master = master
        master.title("Bookbot++")
        master.geometry("500x300")

        # State variables
        self.file_path = None
        self.filter_var = tk.DoubleVar(value=0)

        # *Create UI elements
        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        """Create UI elements."""
        # Create a bold font for labels
        bold_font = font.Font(weight="bold")

        # *File selection
        self.file_select = ttk.Button(
            self.master, text="Select a File", command=self._select_file)
        self.file_label = ttk.Label(
            self.master, text="Selected file:", font=bold_font)
        self.file = ttk.Label(self.master)

        # *Filter results
        self.filter_label = ttk.Label(
            self.master, text="Present to other 0%", font=bold_font)
        self.filter_slider = ttk.Scale(
            self.master, variable=self.filter_var, from_=0, to=100, length=150, orient="horizontal", command=self._update_filter_label)
        self.description = ttk.Label(
            text=f"Other% means any items that are below the percent are combined into one bar in the graph")

        # *Submit Button
        self.submit_button = ttk.Button(
            self.master, text="Show graph", command=self._submit)

    def _layout_widgets(self):
        """Pack/place/grid UI elements."""
        self.file_select.pack()
        self.file_label.pack()
        self.file.pack()
        self.filter_label.pack()
        self.filter_slider.pack()
        self.description.pack()
        self.submit_button.pack()

    # HELPER FUNCTIONS

    def _select_file(self):
        """Open a file dialog to select a file."""
        path = filedialog.askopenfilename(filetypes=(
            ("Text files", "*.txt"), ("All files", "*.*")))
        if path:
            self.file_path = path
            file_name = path.split("/")[-1]
            self.file.config(text=file_name)

    def _update_filter_label(self, event):
        """Update the filter label when the slider is moved."""
        self.filter_label.config(
            text=f"Present to other: {int(self.filter_var.get())}%")

    def _submit(self):
        """Gather data from screen and switch to new screen"""
        # FIXME: Added the function to clear the screen

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()
