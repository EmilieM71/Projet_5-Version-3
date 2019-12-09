from config import CATEGORY
from model.Manage_db import ManageDb
from view.view2_steps import ViewSteps


class ControllerSteps:
    """ This class is:
        - the link with the 'start view' """
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.model = ManageDb()
        self.view = ViewSteps(self)
        self.cnx = None

    def shows_steps_view(self):
        """ this method shows the steps vue"""
        self.view.open_view_steps()

    def connect_to_mysql(self, can):
        self.cnx = self.model.connection_mysql()
        self.controller.cnx = self.cnx
        self.view.create_widgets_connect_to_mysql(can, self.cnx)

    def connect_to_db(self, can):
        connect_db = self.model.connection_db()
        self.view.create_widgets_connect_db(can, connect_db)

    def back_start_for_create_user(self):
        self.controller.cont_start.show_start_view_user()

    def create_db(self):
        create_db = self.model.create_db()
        return create_db

    def search_presence_api_data_in_db(self, can):
        presence_data = self.model.search_presence_api_data_in_database()
        self.view.create_widgets_presence_data(can, presence_data)
        pass

    def return_to_the_start_view(self):
        self.controller.cont_start.create_db()

    def login(self):
        self.controller.cont_user.show_user_view()

    def download_data(self):
        for cat in CATEGORY:
            print(cat)
            products = self.model.download_api_data(cat)
            self.model.insert_data_in_tables(products)
            self.login()
