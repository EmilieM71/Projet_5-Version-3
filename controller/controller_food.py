from model.tables_db.manage_tables import ManageTables
from view.view6_select_food import ViewSelectFood


class ControllerFood:
    """ This class is the link with :
        - the 'select food view'
        - the food table in database"""
    def __init__(self, cont):
        """
        :param cont: ManageController
        """
        self.controller = cont
        self.tables = ManageTables(cont.cnx)
        self.view = ViewSelectFood(self)

    def show_select_food(self, info_cat):
        """ This method display the selected food and substitute view"""
        list_food = self.tables.food_manager.recover_food_name_list(
            info_cat[0])
        self.view.open_view_select_food(info_cat[1], list_food)

    def show_sub_view(self):
        list_food_sub_id = self.tables.user_food_manager.\
            search_data_in_table_for_user(self.controller.info_user[0])
        list_search = []
        for id_food_sub in list_food_sub_id:
            search = []
            for id_food in id_food_sub:
                name_food = self.tables.food_manager.get_name(id_food)
                search.append(name_food)
            list_search.append(search)
        self.view.show_sub_view(list_search)

    def back_to_the_menu(self):
        """ This method returns to the menu: welcome view """
        self.controller.cont_welcome.show_welcome_view()

    def back_to_select_cat(self):
        """ This method returns to the selected category view """
        self.controller.cont_cat.show_select_cat_view()

    def recover_info_food(self, id_food):
        """ this method recover food information"""
        info_food = self.tables.food_manager.recover_info_food(id_food)
        return info_food

    def displays_food_information(self, selected_food):
        """ This method display food information """
        id_food = self.tables.food_manager.get_id(selected_food)
        return id_food

    def recover_list_of_id_cat(self, id_food):
        """ This method retrieves the list of categories in the database from
        the food id"""
        list_id_cat = self.tables.food_manager.recover_id_cat_list(id_food)
        return list_id_cat

    def recover_store_name_list(self, id_food):
        """ This method retrieves the list of stores in the database from
        the food id"""
        list_store = self.tables.store_manager.recover_store_name_list(id_food)
        return list_store

    def recover_brand_name_list(self, id_food):
        """ This method retrieves the list of brands in the database from
        the food id"""
        list_brand = self.tables.brand_manager.recover_brand_name_list(id_food)
        return list_brand

    def substitute_research(self, nutriscore, score_nutri, nova):
        """ This method searches for a substitute from the category,
        nutriscore and nova group"""
        list_substitute = self.tables.food_manager.substitute_research(
            self.controller.selected_category[0], nutriscore, score_nutri,
            nova)
        return list_substitute

    def save_research(self, id_food, id_sub):
        """ This method saves the search in the database """
        self.tables.user_food_manager.search_if_research_exist(
            user_id=self.controller.info_user[0], food_id=id_food,
            substitute_id=id_sub)
        self.back_to_the_menu()
