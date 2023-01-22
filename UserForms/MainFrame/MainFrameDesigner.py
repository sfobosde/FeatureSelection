from tkinter import *
from UserForms.IFormDesigner import IFormDesigner
from UserForms.IFrame import IFrame


class MainFrameDesigner(IFormDesigner):
    def __init__(self, window: Tk):
        self.window = window
        self.initialize_form()

    def initialize_form(self):
        self.add_label("test")

