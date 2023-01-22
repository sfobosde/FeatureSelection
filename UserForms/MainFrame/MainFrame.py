from tkinter import *
from UserForms.IFrame import IFrame
from UserForms.MainFrame.MainFrameDesigner import MainFrameDesigner


# Realise mainFrame interface.
class MainFrame(IFrame):
    def __init__(self, title="Unnamed Form", size='800x600'):
        self.window = Tk()
        self.window.geometry(size)
        self.window.title(title)
        self.__designer = MainFrameDesigner(self.window)

    def show(self):
        if (self.window):
            self.window.mainloop()
        else:
            raise Exception("Window not initialized")

    def handle_error(self, error:Exception):
        error_frame = Tk()

        error_label = LabelFrame(error_frame, text="Возникла ошибка при выполнении действия.")
        error_label.pack(fill="both", expand="yes")

        error_text = Label(error_label, text=error)
        error_text.pack()

        error_label.mainloop()
