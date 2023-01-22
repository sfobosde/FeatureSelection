from Entities.IFeatureSelectionCore import IFeatureSelectionCore
from UserForms.MainFrame.IMainFrame import IMainFrame


class Presenter:
    mainFrame: IMainFrame
    featureSelectionCore: IFeatureSelectionCore

    def __init__(self, main_frame, feature_selection_core):
        self.mainFrame = main_frame
        self.featureSelectionCore = feature_selection_core

        # Connect events -> handlers.
        self.mainFrame.add_dataset_file.add_handler(self.featureSelectionCore.receive_dataset_file)
        self.featureSelectionCore.show_dataframe.add_handler(self.mainFrame.receive_dataset)

        try:
            self.mainFrame.show()
        except Exception as e:
            self.mainFrame.handle_error(e)

