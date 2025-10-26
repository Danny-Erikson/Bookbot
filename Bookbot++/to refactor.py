# Used for plotting graphs
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funtions for analyzing books, See stats.py for more details
from stats import count_words
from stats import count_characters
from stats import filter


# Initialize Tkinter
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()


def get_book_text(path):
    # Used to import a book to be analyzed
    with open(path) as f:
        return f.read()


def on_close():
    plt.close(fig)
    root.destroy()


def file_selection():
    file_path = filedialog.askopenfilename()
    return file_path


def main():
    frame = tk.Frame(root)
    label = tk.Label(frame, text="File name")
    label.config(font=("Courier", 32))
    file_select.pack()
    label.pack()
    frame.pack()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


def testing():
    # Start the progarm
    # text = get_book_text()

    # Word Count
    num_words = count_words(text)

    # Character Count
    char_dict = count_characters(text)

    # FIXME: Take num_words and char_dict and make it output to the graph
