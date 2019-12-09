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
        self.controller.cont_steps.shows_steps_view()

    def show_start_view_user(self):
        self.view.show_start_view_user()

    def create_db(self):
        self.view.create_db()
