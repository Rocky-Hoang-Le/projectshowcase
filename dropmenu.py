import tkinter as tk
from tkinter import ttk


class CreateMenu:
    def __init__(self, tab):
        self.mainframe = tk.Frame(tab)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack(pady=100, padx=100)
