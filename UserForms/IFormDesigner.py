from tkinter import *
from tkinter.ttk import Label


class IFormDesigner:
    window: Tk = None

    def add_label(self, label_text="", column=0, row=0):
        label = Label(self.window, text=label_text)
        label.grid(column=column, row=row)

    def initialize_form(self):
        pass
