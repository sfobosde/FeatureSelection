from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd


class FeatureSelectionCore(IFeatureSelectionCore):
    def receive_dataset_file(self, file):
        if (file):
            self.__file = file
            dataframe = pd.read_csv(file)
