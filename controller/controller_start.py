from view.view1_start import ViewStart


class ControllerStart:
    """ This class is:
        - the link with the 'start view' """
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.view = ViewStart(self)

    def shows_start_view(self):
        """ this method shows the start vue"""
        self.view.open_view_start()

    def shows_steps_view(self):
        pass
