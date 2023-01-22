from Entities.IEntityManager import IEntityManager
from UserForms.IFrame import IFrame


class Presenter:
    mainFrame: IFrame
    entityManager: IEntityManager

    def __init__(self, IMainFrame, IEntityManager):
        self.mainFrame = IMainFrame
        self.entityManager = IEntityManager
        try:
            self.mainFrame.show()
        except Exception as e:
            self.mainFrame.handle_error(e)

