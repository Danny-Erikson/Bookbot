import tkinter as tk
from Bookbot_app import BookBotApp


def main():
    root = tk.Tk()
    app = BookBotApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
