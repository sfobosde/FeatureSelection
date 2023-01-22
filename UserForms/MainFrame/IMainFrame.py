from Event import UserEvent
from UserForms.IFrame import IFrame


class IMainFrame(IFrame):
    # The event calling core handle and send dataset file.
    add_dataset_file: UserEvent

    # The list of exclude columns names.
    drop_columns_list: list

    # Catch read by core dataset.
    def receive_dataset(self, dataset):
        pass

    # Add column to exclude list.
    def add_to_droplist(self, column_name):
        pass

    # Remove column from exclude list.
    def remove_from_droplist(self, column_name):
        pass
