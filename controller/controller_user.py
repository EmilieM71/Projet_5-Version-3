from model.user import User
from view.view3_login import ViewLogin


class ControllerUser:
    """ This class is:
        - the link with the 'user view'
        - the link with user table"""
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.model = User(cont.cnx, self)
        self.view = ViewLogin(self)

    def show_user_view(self):
        self.view.open_view_login()

    def create_user(self, pseudo2, password, email):
        id_user = self.model.create_user(email, pseudo2, password)
        self.controller.info_user = (id_user, pseudo2)
        self.controller.cont_cat.show_select_cat_view()

    def search_if_pseudo_exist(self, pseudo2):
        pass

    def verify_if_user_exists(self, pseudo, password):
        id_user = self.model.search_if_user_exist(pseudo, password)
        self.controller.info_user = (id_user, pseudo)
        return self.controller.info_user

    def select_cat(self):
        self.controller.cont_cat.show_select_cat_view()
