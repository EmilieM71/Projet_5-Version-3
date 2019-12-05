class ControllerSteps:
    """ This class is:
        - the link with the 'start view' """
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.model = None
        self.view = None