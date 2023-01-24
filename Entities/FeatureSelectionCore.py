from matplotlib import pyplot as plt

from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd
import seaborn as sns

from Event import UserEvent


# Calculation core class.
class FeatureSelectionCore(IFeatureSelectionCore):
    __excluding_columns: list

    def __init__(self):
        self.show_dataset = UserEvent()
        self.show_cleaned_dataset = UserEvent()
        self.throw_exception = UserEvent()

        self.__excluding_columns = list()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, ds_file):
        if ds_file:
            self.dataset = pd.read_csv(ds_file)
            self.cleaned_dataset = self.dataset

            self.show_dataset(self.dataset)

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        self.__excluding_columns = columns
        self.exclude_columns()
        self.show_cleaned_dataset(self.cleaned_dataset)

    def exclude_columns(self):
        if not len(self.__excluding_columns):
            self.__excluding_columns.append(self.dataset.columns[0])
            self.throw_exception("Key column did not selected. First column selected as key by default.")

        self.cleaned_dataset = self.dataset.drop(self.__excluding_columns, axis=1)

    # Standardize handler.
    def handle_standardize(self, key_column):
        self.standardize_dataset(key_column)

    # Standardize dataset.
    def standardize_dataset(self, key_column: str):
        column = self.dataset[key_column]
        self.standardized_dataset = (self.cleaned_dataset - self.cleaned_dataset.mean()) / (self.cleaned_dataset.std())

        data = pd.concat([column, self.standardized_dataset.iloc[:, 0:10]], axis=1)
        data = pd.melt(data, id_vars=key_column,
                       var_name="features",
                       value_name='value')

    # Calculations start event.
    def start_calculations(self):
        pass

