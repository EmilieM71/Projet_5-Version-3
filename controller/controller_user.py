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
        self.pseudo = None

    def show_user_view(self):
        self.view.open_view_login()

    def create_user(self, pseudo2, password, email):
        id_user = self.model.create_user(email, pseudo2, password)
        self.controller.info_user = (id_user, pseudo2)
        self.controller.cont_cat.show_select_cat_view()

    def search_if_pseudo_exist(self, pseudo):
        pseudo = self.model.search_if_pseudo_exist(pseudo)
        self.pseudo = pseudo

    def search_if_user_exist(self, pseudo, password):
        self.pseudo = self.model.search_if_user_exist(pseudo, password)
        self.controller.pseudo = self.pseudo
        return self.pseudo

    def choice_welcome(self):
        self.controller.cont_welcome.show_welcome_view(self.pseudo)
        self.controller.pseudo = self.pseudo
