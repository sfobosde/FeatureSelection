from Entities.FeatureSelectionCore import FeatureSelectionCore
from Presenter import Presenter
from UserForms.MainFrame.MainFrame import MainFrame

# Create frame object.
main_frame = MainFrame("Feature Selection", '1280x720')

# Create entity manager  object.
feature_selection_core = FeatureSelectionCore()

# Create presenter.
presenter = Presenter(main_frame, feature_selection_core)
