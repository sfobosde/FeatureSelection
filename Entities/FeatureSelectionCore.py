from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd

from Event import UserEvent


# Calculation core class.
class FeatureSelectionCore(IFeatureSelectionCore):
    def __init__(self):
        self.show_dataset = UserEvent()
        self.show_cleaned_dataset = UserEvent()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, ds_file):
        if ds_file:
            # Read CSV file and send it to form.
            self.dataset = pd.read_csv(ds_file)
            self.cleaned_dataset = self.dataset
            self.show_dataset(self.dataset)

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        self.cleaned_dataset = self.dataset.drop(columns, axis=1)
        self.show_cleaned_dataset(self.cleaned_dataset)

    # Standardize handler.
    def handle_standardize(self, key_column):
        self.standardize_dataset(key_column)

    # Standardize dataset.
    def standardize_dataset(self, key_column):
        print(f"key column: {key_column}")
        column = self.dataset[key_column]
        self.standardized_dataset = (self.cleaned_dataset - self.cleaned_dataset.mean()) / (self.cleaned_dataset.std())

        data = pd.concat([column, self.standardized_dataset.iloc[:, 0:10]], axis=1)
        data = pd.melt(data, id_vars=key_column,
                       var_name="features",
                       value_name='value')

    def show_graph(self):
        pass


