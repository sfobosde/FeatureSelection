from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd

from Event import UserEvent


class FeatureSelectionCore(IFeatureSelectionCore):
    def __init__(self):
        self.show_dataframe = UserEvent()

    def receive_dataset_file(self, file):
        if (file):
            self.__file = file
            dataframe = pd.read_csv(file)
            self.show_dataframe(dataframe)
