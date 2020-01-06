from config import CATEGORY
from model.manage_db.create_db import CreateDatabase
from model.manage_db.insert_data_in_db import InsertData
from view.view2_steps import ViewSteps


class ControllerSteps:
    """ This class is:
        - the link with the 'start view' """
    model = InsertData()

    def __init__(self, cont):
        """

        :param cont: ManageController
        """
        self.cont = cont
        self.cnx = None
        self.view = ViewSteps(self)
        self.create_db = None

    def display_start_steps(self):
        """ this method shows the steps vue"""
        self.view.open_view_steps()

    def connect_to_mysql(self, can):
        self.cnx = self.cont.cnx
        self.view.create_widgets_connect_to_mysql(can, self.cnx)

    def connect_to_db(self, can):
        self.create_db = CreateDatabase(self.cont.cnx)
        connect_db = self.create_db.connection_db(cursor=None)
        self.view.create_widgets_connect_db(can, connect_db)

    def back_start_for_create_user(self):
        self.cont.cont_start.show_start_view_user()

    def create_database(self):
        create_db = self.create_db.create_db_with_file()
        return create_db

    def search_presence_api_data_in_db(self, can):
        self.create_db.connection_db(cursor=None)
        presence_data = self.model.search_presence_api_data_in_database()
        self.view.create_widgets_presence_data(can, presence_data)

    # @classmethod
    # def return_to_the_start_view(cls):
    #     ManageController.cont_start.create_db()
    #
    def login(self):
        self.cont.cont_user.show_user_view()

    def download_data(self):
        for cat in CATEGORY:
            print(cat)
            products = self.model.download_api_data(cat)
            self.model.insert_data_in_tables(products)
            self.login()
