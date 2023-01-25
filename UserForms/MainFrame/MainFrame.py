from tkinter import *
from tkinter.filedialog import askopenfile

from Event import UserEvent
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
        self.drop_included_columns = UserEvent()
        self.get_bar_graph = UserEvent()
        self.standardize_dataset = UserEvent()
        self.calculate_statistics = UserEvent()
        self.key_column_selected = UserEvent()

        self.__drop_list = []

    # Show generated form.
    def show(self):
        if self.window:
            self.window.mainloop()
        else:
            raise Exception("Window not initialized")

    # Catch errors.
    def handle_error(self, error: Exception):
        error_frame = Tk()

        error_label = LabelFrame(error_frame, text="Error occurred in runtime.")
        error_label.pack(fill="both")

        error_text = Label(error_label,
                           text=str(error))
        error_text.pack()

        error_label.mainloop()

    # Handle load dataset button click.
    def load_button_clicked(self):
        # filetypes=(("CSV Files", "*.csv"),)
        file = askopenfile(filetypes=(("CSV Files", "*.csv"),))
        if file:
            try:
                self.add_dataset_file(file)
            except Exception as e:
                self.handle_error(e)

    # Catch read by core dataset.
    def receive_dataset(self, dataset):
        # Call designer method to visualise dataset.
        self.__designer.visualise_dataset(dataset)

    # Add column to exclude list.
    def add_to_dl(self, column_name):
        self.__drop_list.append(column_name)

    # Remove column from exclude list.
    def remove_from_dl(self, column_name):
        self.__drop_list.remove(column_name)

    # Drop included columns.
    def drop_columns(self):
        print(self.__drop_list)
        self.drop_included_columns(self.__drop_list)

    # Catch cleaned by core dataset.
    def show_cleaned_dataframe(self, dataset):
        self.__designer.show_cleaned_dataset(dataset)

    # Normalize (standardize) data.
    def calculate_normalized(self):
        self.standardize_dataset(self.__designer.get_column_name())

    # Handler of starting calculations.
    def start_calculation(self):
        self.calculate_statistics()

