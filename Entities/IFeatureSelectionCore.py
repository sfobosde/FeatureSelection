from Event import UserEvent


class IFeatureSelectionCore:
    # The event to throw dataframe to view.
    show_dataframe: UserEvent()

    # The event to throw cleaned dataframe to view.
    show_cleaned_dataframe: UserEvent()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, file):
        pass

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        pass
