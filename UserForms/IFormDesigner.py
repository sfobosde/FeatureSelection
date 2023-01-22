from tkinter import *
from tkinter.ttk import Label

from UserForms.IFrame import IFrame


class IFormDesigner:
    frame: IFrame = None
    window: Tk = None

    def add_label(self, frame, label_text="", padx=0, pady=0, side=LEFT, font=("Arial", 14)):
        pass

    def add_button_text(self, frame, click_handler, text='Click Me!', padx=0, pady=0, side=LEFT):
        pass

    def create_frame(self, anchor=NW, border_width=0, relief=SOLID, padx=0, pady=0):
        pass

    def initialize_form(self):
        pass
