from Entities.EntityManager import EntityManager
from Presenter import Presenter
from UserForms.MainFrame.MainFrame import MainFrame

main_frame = MainFrame("Feature Selection", '800x600')
entity_manager = EntityManager()

presenter = Presenter(main_frame, entity_manager)
