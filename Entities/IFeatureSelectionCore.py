from pandas import DataFrame
from Event import UserEvent


class IFeatureSelectionCore:
    # The event to throw dataframe to view.
    show_dataset: UserEvent()

    # The event to throw cleaned dataframe to view.
    show_cleaned_dataset: UserEvent()

    # Original dataframe.
    dataset: DataFrame

    # Purified data frame.
    cleaned_dataset: DataFrame

    # Normalized (standardized) dataset.
    standardized_dataset: DataFrame

    # Violoned dataset.
    violoned_dataset: DataFrame

    # Raise exception.
    throw_exception: UserEvent

    # Handle event and catch dataset file.
    def receive_dataset_file(self, file):
        pass

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        pass

    # Standardize dataset.
    def standardize_dataset(self):
        pass

    # Standardize handler.
    def handle_standardize(self, key_column):
        pass

    # Calculations start event.
    def start_calculations(self):
        pass

    # Get selected key column.
    def catch_key_column(self, key_column):
        pass
