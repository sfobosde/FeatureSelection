from Entities.IFeatureSelectionCore import IFeatureSelectionCore
import pandas as pd

from Event import UserEvent


# Calculation core class.
class FeatureSelectionCore(IFeatureSelectionCore):
    def __init__(self):
        self.show_dataframe = UserEvent()

    # Handle event and catch dataset file.
    def receive_dataset_file(self, ds_file):
        if ds_file:
            # Read CSV file and send it to form.
            dataframe = pd.read_csv(ds_file)
            self.show_dataframe(dataframe)
