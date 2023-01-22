from tkinter import *
from tkinter.ttk import Label

from UserForms.IFrame import IFrame


class IFormDesigner:
    frame: IFrame = None
    window: Tk = None

    def add_label(self, label_text="", padx=0, pady=0, side=LEFT, anchor="nw", font=("Arial", 14)):
        label = Label(self.window, text=label_text, font=font)
        label.pack(
            anchor=anchor,
            padx=padx,
            pady=pady,
            side=side,)

    def add_button_text(self, click_handler, text='Click Me!', padx=0, pady=0, side=LEFT, anchor='nw'):
        button = Button(self.window, text=text, command=click_handler)
        button.pack(
            anchor=anchor,
            padx=padx,
            pady=pady,
            side=side)

    def initialize_form(self):
        pass
