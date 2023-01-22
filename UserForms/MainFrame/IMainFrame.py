from Event import UserEvent
from UserForms.IFrame import IFrame


class IMainFrame(IFrame):
    add_dataset_file: UserEvent

    def receive_dataset(self, dataset):
        pass
