from tkinter import *
from tkinter.ttk import Label

from UserForms.IFrame import IFrame


class IFormDesigner:
    frame: IFrame = None
    window: Tk = None

    def add_label(self, label_text="", column=0, row=0, font=("Arial", 14)):
        label = Label(self.window, text=label_text, font=font)
        label.grid(column=column, row=row)

    def add_button_text(self, click_handler, text='Click Me!', column=0, row=0):
        button = Button(self.window, text=text, command=click_handler)
        button.grid(column=column, row=row)

    def initialize_form(self):
        pass
