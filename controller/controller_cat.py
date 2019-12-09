from model.category import Category
from view.view5_select_cat import ViewSelectCat


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
        self.view = ViewSelectCat(self)

    def show_select_cat_view(self, pseudo):
        self.controller.pseudo = pseudo
        self.view.open_view_select_cat()

    def back_to_the_menu(self):
        self.controller.cont_welcome.show_welcome_view(self.controller.pseudo)

    def get_id_selected_category(self, cat):
        id_cat = self.model.get_id(cat)
        self.controller.info_cat = (id_cat, cat)
        self.controller.cont_food.show_select_food(self.controller.pseudo,
                                                   self.controller.info_cat)
