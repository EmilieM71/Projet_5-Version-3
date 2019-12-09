from view.view4_welcome import ViewWelcome


class ControllerWelcome:
    """ This class is:
            - the link with the 'welcome view'"""

    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.view = ViewWelcome(self)

    def show_welcome_view(self, pseudo):
        self.controller.pseudo = pseudo
        self.view.open_view_welcome()

    def find_substitute(self):
        self.controller.cont_cat.show_select_cat_view(self.controller.pseudo)

    def review_substitute(self):
        # self.controller.cont_sub.show_sub_view()
        pass
