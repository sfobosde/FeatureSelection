from tkinter import *
from tkinter.ttk import Label

from UserForms.IFrame import IFrame
from UserForms.MainFrame.IMainFrame import IMainFrame


# Interface of main form designer.
class IFormDesigner:
    frame: IMainFrame = None
    dataset_frame: Frame = None
    window: Tk = None

    # Methods.
    def add_label(self, frame, label_text="", padx=0, pady=0, side=LEFT, font=("Arial", 14)):
        pass

    def add_button_text(self, frame, click_handler, text='Click Me!', padx=0, pady=0, side=LEFT):
        pass

    def create_frame(self, frame, anchor=NW, border_width=0, relief=SOLID, padx=0, pady=0):
        pass

    def initialize_form(self):
        pass
