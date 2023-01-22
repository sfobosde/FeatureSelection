# Main Frame interface.
from tkinter import Tk


class IMainFrame:
    window: Tk = None

    def show(self):
        pass

    def handle_error(self, error):
        pass
