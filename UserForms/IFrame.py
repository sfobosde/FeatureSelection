# Main Frame interface.
from tkinter import Tk


class IFrame:
    # Window type object.
    window: Tk = None

    def show(self):
        pass

    def handle_error(self, error):
        pass

    def load_button_clicked(self):
        pass
