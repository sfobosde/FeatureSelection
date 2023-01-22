from Event import UserEvent
from UserForms.IFrame import IFrame


class IMainFrame(IFrame):
    add_dataset_file: UserEvent
    drop_columns_list: list

    def receive_dataset(self, dataset):
        pass

    def add_to_droplist(self, column_name):
        pass

    def remove_from_droplist(self, column_name):
        pass
