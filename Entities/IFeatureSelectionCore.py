from Event import UserEvent


class IFeatureSelectionCore:
    show_dataframe: UserEvent()

    def receive_dataset_file(self, file):
        pass
