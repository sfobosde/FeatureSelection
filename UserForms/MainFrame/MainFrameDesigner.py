from tkinter import *
from UserForms.IFormDesigner import IFormDesigner
from UserForms.IFrame import IFrame


class MainFrameDesigner(IFormDesigner):
    def __init__(self, frame: IFrame):
        self.window = frame.window
        self.frame = frame
        self.initialize_form()

    def initialize_form(self):
        self.add_label("Загрузите выборку:", 0, 0, ("Arial", 11))
        self.add_button_text(click_handler=self.frame.load_button_clicked, text="Загрузить", column=2, row=0)

