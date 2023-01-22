from Entities.FeatureSelectionCore import FeatureSelectionCore
from Presenter import Presenter
from UserForms.MainFrame.MainFrame import MainFrame

# Create frame object.
main_frame = MainFrame("Feature Selection", '800x600')

# Create entity manager  object.
feature_selection_core = FeatureSelectionCore()

# Create presentor.
presenter = Presenter(main_frame, feature_selection_core)
