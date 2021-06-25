import tkinter as tk
from tkinter import ttk


class CreateTabs(ttk.Notebook):
    def __init__(self, parent, **kwargs):
        ttk.Notebook.__init__(self, master=parent, **kwargs)
        self.parent = parent

    def create_tab(self):
        return ttk.Frame(self)



