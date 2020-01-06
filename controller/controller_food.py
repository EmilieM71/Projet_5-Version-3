from model.tables_db.manage_tables import ManageTables
from view.view6_select_food import ViewSelectFood


class ControllerFood:
    """ This class is:
        - the link with the 'select food view'
        - the link with food table"""
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.tables = ManageTables(cont.cnx)
        self.view = ViewSelectFood(self)

    def show_select_food(self, pseudo, info_cat):
        self.controller.pseudo = pseudo
        list_food = self.tables.food_manager.recover_food_name_list(
            info_cat[0])
        self.view.open_view_select_food(info_cat[1], list_food)

    def back_to_the_menu(self):
        self.controller.cont_welcome.show_welcome_view(self.controller.pseudo)

    def back_to_select_cat(self, pseudo):
        self.controller.cont_cat.show_select_cat_view(pseudo)

    def recover_info_food(self, id_food):
        info_food = self.tables.food_manager.recover_info_food(id_food)
        return info_food

    def displays_food_information(self, selected_food):
        id_food = self.tables.food_manager.get_id(selected_food)
        return id_food

    def recover_list_of_id_cat(self, id_food):
        list_id_cat = self.tables.food_manager.recover_id_cat_list(id_food)
        return list_id_cat

    def recover_store_name_list(self, id_food):
        list_store = self.tables.store_manager.recover_store_name_list(id_food)
        return list_store

    def recover_brand_name_list(self, id_food):

        list_brand = self.tables.brand_manager.recover_brand_name_list(id_food)
        return list_brand

    def substitute_research(self, nutriscore, score_nutri, nova):
        list_substitute = self.tables.food_manager.substitute_research(
            self.controller.selected_category[0], nutriscore, score_nutri,
            nova)
        return list_substitute

    def save_research(self, id_food, id_sub):

        self.tables.user_food_manager.search_if_research_exist(
            user_id=self.controller.pseudo, food_id=id_food,
            substitute_id=id_sub)
        self.back_to_the_menu()
