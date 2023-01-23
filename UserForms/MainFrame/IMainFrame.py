from Event import UserEvent
from UserForms.IFrame import IFrame


class IMainFrame(IFrame):
    # The event calling core handle and send dataset file.
    add_dataset_file: UserEvent

    # The event to drop columns.
    drop_included_columns: UserEvent

    # Get bar graph of column.
    get_bar_graph: UserEvent

    # Normalize data.
    nomalize_data: UserEvent

    # The list of exclude columns names.
    __drop_list: list

    # Catch read by core dataset.
    def receive_dataset(self, dataset):
        pass

    # Add column to exclude list.
    def add_to_dl(self, column_name):
        pass

    # Remove column from exclude list.
    def remove_from_dl(self, column_name):
        pass

    # Drop included columns.
    def drop_columns(self):
        pass

    # Catch cleaned by core dataset.
    def show_cleaned_dataframe(self, dataset):
        pass

    # Handle choice in radiobutton.
    def column_selected(self):
        pass
