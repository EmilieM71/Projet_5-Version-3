from view.view3_login import ViewLogin
from model.tables_db.user_manager import UserManager


class ControllerUser:
    """ This class is:
        - the link with the 'user view'
        - the link with user table in database """

    def __init__(self, cont):
        """

        :param cont: ManageController
        """
        self.controller = cont
        self.view = ViewLogin(self)
        self.model = UserManager(self.controller.cnx)
        self.info_user = None

    def show_user_view(self):
        self.view.open_view_login()

    def create_user(self, pseudo2, password, email):
        id_user = self.model.create_user(email, pseudo2, password)
        self.info_user = (id_user, pseudo2)
        self.controller.info_user = self.info_user
        self.controller.cont_cat.show_select_cat_view()

    def search_if_pseudo_exist(self, pseudo):
        id_user = self.model.search_if_pseudo_exist(pseudo)
        self.info_user = (id_user, pseudo)

    def search_if_user_exist(self, pseudo, password):
        id_user = self.model.search_if_user_exist(pseudo, password)
        self.info_user = (id_user, pseudo)
        self.controller.info_user = self.info_user
        return self.info_user

    def choice_welcome(self):
        self.controller.cont_welcome.show_welcome_view(self.info_user)
