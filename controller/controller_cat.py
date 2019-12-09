from model.category import Category
from view.view3_login import ViewLogin


class ControllerCat:
    """ This class is:
        - the link with the 'user view'
        - the link with user table"""
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.model = Category(cont.cnx, self)
        self.view = ViewSelectCat(self, cont.info_user)

    def show_user_view(self):
        self.view.open_view_select_cat()
