from Entities.IEntityManager import IEntityManager
from UserForms.IMainFrame import IMainFrame


class Presenter:
    mainFrame: IMainFrame
    entityManager: IEntityManager

    def __init__(self, IMainFrame, IEntityManager):
        self.mainFrame = IMainFrame
        self.entityManager = IEntityManager
        try:
            self.mainFrame.show()
        except Exception as e:
            self.mainFrame.handle_error(e)

