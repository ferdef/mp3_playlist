from log import logger
import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import filedialog


def process(args):
    window = Window()
    window.create_window()
    window.create_widgets()
    window.mainloop()


class Window:
    def __init__(self):
        pass

    def mainloop(self):
        self.win.mainloop()

    def create_window(self):
        win = tk.Tk()
        win.title("MP3 Playlist")
        win.resizable(False, False)
        self.win = win

    def create_widgets(self):
        ttk.Label(self.win, text="Source").grid(column=0, row=0)
        ttk.\
            Entry(self.win).\
            grid(column=0, row=1)
        ttk.\
            Button(self.win, text="...", command=browse_source).\
            grid(column=1, row=1)
        scrolledtext.\
            ScrolledText(self.win, width=30, height=3).\
            grid(column=0, row=2, columnspan=2)
        ttk.Label(self.win, text="Destination").grid(column=0, row=3)
        ttk.\
            Entry(self.win).\
            grid(column=0, row=4)
        ttk.\
            Button(self.win, text="...", command=browse_source).\
            grid(column=1, row=4)
        ttk.\
            Progressbar(self.win, orient='horizontal').\
            grid(column=0, row=5, columnspan=2)


def browse_source():
    filedialog.askdirectory()
