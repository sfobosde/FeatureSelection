from matplotlib import pyplot as plt

from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd
import seaborn as sns

from Event import UserEvent


# Calculation core class.
class FeatureSelectionCore(IFeatureSelectionCore):
    __excluding_columns: list
    key_column: str

    def __init__(self):
        self.show_dataset = UserEvent()
        self.show_cleaned_dataset = UserEvent()
        self.throw_exception = UserEvent()

        self.__excluding_columns = list()

        self.key_column = str()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, ds_file):
        if ds_file:
            self.dataset = pd.read_csv(ds_file)
            self.cleaned_dataset = self.dataset

            self.show_dataset(self.dataset)

    # Get selected key column.
    def catch_key_column(self, key_column):
        self.key_column = key_column

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        self.__excluding_columns = columns
        self.exclude_columns()
        self.show_cleaned_dataset(self.cleaned_dataset)

    def exclude_columns(self):
        if not len(self.__excluding_columns):
            self.__excluding_columns.append(self.dataset.columns[0])

        self.cleaned_dataset = self.dataset.drop(self.__excluding_columns, axis=1)

    # Standardize handler.
    def handle_standardize(self, key_column):
        self.key_column = key_column
        self.standardize_dataset()

    # Standardize dataset.
    def standardize_dataset(self):
        if not self.key_column:
            self.key_column = self.dataset.columns[0]

        column = self.dataset[self.key_column]
        data = (self.cleaned_dataset - self.cleaned_dataset.mean()) / (self.cleaned_dataset.std())

        data = pd.concat([column, data.iloc[:, 0:10]], axis=1)
        self.standardized_dataset = pd.melt(data, id_vars=self.key_column,
                                            var_name="features",
                                            value_name='value')

    # Calculations start event.
    def start_calculations(self):
        self.exclude_columns()
        self.show_cleaned_dataset(self.cleaned_dataset)
        self.standardize_dataset()
        self.show_cleaned_dataset(self.standardized_dataset)

