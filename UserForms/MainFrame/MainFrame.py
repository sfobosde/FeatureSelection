from tkinter import *
from tkinter.filedialog import askopenfile

from Event import UserEvent
from UserForms.IFrame import IFrame
from UserForms.MainFrame.IMainFrame import IMainFrame
from UserForms.MainFrame.MainFrameDesigner import MainFrameDesigner


# Realise mainFrame interface.
class MainFrame(IMainFrame):
    # Initialize form and generate interface with frame designer.
    def __init__(self, title="Unnamed Form", size='800x600'):
        self.window = Tk()
        self.window.geometry(size)
        self.window.title(title)
        self.__designer = MainFrameDesigner(self)
        self.add_dataset_file = UserEvent()

    # Show generated form,
    def show(self):
        if (self.window):
            self.window.mainloop()
        else:
            raise Exception("Window not initialized")

    # Catch errors.
    def handle_error(self, error: Exception):
        error_frame = Tk()

        error_label = LabelFrame(error_frame, text="Возникла ошибка при выполнении действия.")
        error_label.pack(fill="both", expand="yes")

        error_text = Label(error_label, text=error)
        error_text.pack()

        error_label.mainloop()

    # Handle load dataset button click.
    def load_button_clicked(self):
        file = askopenfile(filetypes=(("CSV Files", "*.csv"),))
        if (file):
            try:
                self.add_dataset_file(file)
            except Exception as e:
                self.handle_error(e)


