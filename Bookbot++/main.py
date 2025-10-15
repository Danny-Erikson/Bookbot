# Used to import a book to be analyzed
import sys

# Used for plotting graphs
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Used for GUI
import tkinter as tk
from tkinter import filedialog

# Funtions for analyzing books, See stats.py for more details
from stats import count_words
from stats import count_characters
from stats import filter

# TODO: refactor the shit out of this code

# Initialize Tkinter
root = tk.Tk()
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


def main():
    #!TESTING
    frame = tk.Frame(root)
    label = tk.Label(frame, text="Hello, Tkinter!")
    label.config(font=("Courier", 32))
    label.pack()
    frame.pack()
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


def testing():
    # Check for correct usage
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    # Start of the program
    print('============ BOOKBOT ============')
    text = get_book_text(sys.argv[1])
    print(f'Analyzing book found at {sys.argv[1]}')

    # Word Count
    num_words = count_words(text)
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')

    # Character Count
    print('--------- Character Count -------')
    char_dict = count_characters(text)
    for i in filter(char_dict):  # *Loop through filtered characters
        print(f'{i['char']}: {i['num']}')
    print('============= END ===============')


# Runtime
if __name__ == "__main__":
    main()
