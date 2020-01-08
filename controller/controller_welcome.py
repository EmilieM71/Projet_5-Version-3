from view.view4_welcome import ViewWelcome
from model.manage_db.disconnection import Disconnection


class ControllerWelcome:
    """ This class is:
            - the link with the 'welcome view'"""

    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.view = ViewWelcome(self)

    def show_welcome_view(self):
        """ This method displays the welcome view """
        self.view.open_view_welcome()

    def find_substitute(self):
        """ This method displays the select a category view """
        self.controller.cont_cat.show_select_cat_view()

    def review_substitute(self):
        """ This method displays the see substitute searches save view """
        self.controller.cont_food.show_sub_view()

    def disconnection_mysql(self):
        """ This method closes the connection to mysql """
        disconnection_mysql = Disconnection(self.controller.cnx)
        disconnection_mysql.__exit__()
