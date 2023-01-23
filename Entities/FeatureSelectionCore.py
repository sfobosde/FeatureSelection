from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd

from Event import UserEvent

import matplotlib.pyplot as plt


# Calculation core class.
class FeatureSelectionCore(IFeatureSelectionCore):
    def __init__(self):
        self.show_dataframe = UserEvent()
        self.show_cleaned_dataframe = UserEvent()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, ds_file):
        if ds_file:
            # Read CSV file and send it to form.
            self.__dataframe = pd.read_csv(ds_file)
            self.show_dataframe(self.__dataframe)

    # The handler of dropping columns from set event.
    def drop_columns(self, columns: list):
        self.__cleaned_dataframe = self.__dataframe.drop(columns, axis=1)
        self.show_cleaned_dataframe(self.__cleaned_dataframe)

