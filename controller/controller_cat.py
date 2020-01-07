from model.tables_db.category_manager import CategoryManager
from view.view5_select_cat import ViewSelectCat


class ControllerCat:
    """ This class is the link with:
        - the 'select category view'
        - the category table in database"""

    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.model = CategoryManager(cont.cnx)
        self.view = ViewSelectCat(self)
        self.info_cat = None

    def show_select_cat_view(self):
        """ This method display the selected category view"""
        pseudo = self.controller.info_user[1]
        self.view.open_view_select_cat(pseudo)

    def back_to_the_menu(self):
        """ This method returns to the menu: welcome view """
        self.controller.cont_welcome.show_welcome_view()

    def get_id_selected_category(self, cat):
        """ This method retrieves the id from the category name """
        id_cat = self.model.get_id(cat)
        self.info_cat = (id_cat, cat)
        self.controller.selected_category = self.info_cat
        self.controller.cont_food.show_select_food(self.info_cat)

