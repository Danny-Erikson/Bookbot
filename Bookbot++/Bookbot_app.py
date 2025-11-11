# Used for plotting
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Used for GUI
import tkinter as tk
from tkinter import ttk, filedialog, font
from stats import count_words, filter, count_characters

# TODO: make the filter option work
# TODO: fix the formatting on the graph
# TODO: fix the formatting on the selection screen


class BookBotApp:
    def __init__(self, master):
        # *Initialization tkinter
        self.master = master
        master.title("Bookbot++")
        master.geometry("500x300")
        master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.fig, self.ax = plt.subplots()

        # State variables
        self.file_contents = None
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
        self.file_name = ttk.Label(self.master)

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
        self.file_name.pack()
        self.filter_label.pack()
        self.filter_slider.pack()
        self.description.pack()
        self.submit_button.pack()

    def _submit(self):
        """Gather data from screen and switch to new screen"""
        # Open the file
        file = open(self.file_path, "r")

        # Clear the screen
        self._clear_frame()

        # Build Stats Screen
        self._stat_widgets()
        self._pack_stat()

    def _stat_widgets(self):
        self.master.geometry("800x600")

        letters = []
        values = []
        char_dict = count_characters(self.file_contents)
        for i in filter(char_dict):
            letters.append(i['char'])
            values.append(i['num'])
        self.ax.bar(letters, values)
        self.ax.set_xlabel('Characters')
        self.ax.set_ylabel('# of Occurrences')

        canvas = FigureCanvasTkAgg(self.fig, self.master)
        self.word_count = ttk.Label(
            text=f"The number of words in {self.file_path.split('/')[-1]} is {count_words(self.file_contents):,}")

        canvas.get_tk_widget().pack()

    def _pack_stat(self):
        self.word_count.pack()

    # HELPER FUNCTIONS

    def on_close(self):
        plt.close(self.fig)
        self.master.destroy()

    def _clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def _select_file(self):
        """Open a file dialog to select a file."""
        path = filedialog.askopenfilename(filetypes=(
            ("Text files", "*.txt"), ("All files", "*.*")))
        if path:
            self.file_path = path
            file_name = path.split("/")[-1]
            self.file_name.config(text=file_name)
            self._update_file_state()

    def _update_file_state(self):
        """Open the file and save the contents to a state variable"""
        with open(self.file_path, "r") as f:
            self.file_contents = f.read()

    def _update_filter_label(self, event):
        """Update the filter label when the slider is moved."""
        self.filter_label.config(
            text=f"Present to other: {int(self.filter_var.get())}%")
