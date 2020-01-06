from config import ARRAY_LINE_REF
from view.manage_view import ManageView
from tkinter import scrolledtext, Text, INSERT
import webbrowser


class ViewSelectFood(ManageView):

    def __init__(self, cont):
        self.controller = cont

        self.list_food = None
        self.frame_food = None
        self.combo_food = None
        self.selected_food = None
        self.label_select_food = None
        self.info_food = None

        self.list_sub = []
        self.combo_sub = None
        self.selected_sub = None
        self.label_select_sub = None
        self.info_sub = None

        self.frame_info = None

    def create_frame_cat(self):
        """ This method creates a frame in the window """
        self.frame_food = self.create_frame(self.root, padx=5)

    def back_to_the_menu(self):
        self.controller.back_to_the_menu()

    def back_choice_cat(self):
        self.controller.back_to_select_cat(self.controller.controller.pseudo)

    def recovers_categories(self, info_food):
        # Insert categories into the list_info_food
        # in table category_food get the list_id_cat
        list_id_cat = self.controller.recover_list_of_id_cat(info_food[0])
        list_name_cat = []
        for id_cat in list_id_cat:
            # recover name cat in list_name_cat
            name_cat = self.controller.recover_name_cat(id_cat)
            list_name_cat.append(name_cat)
        # turn list_name_cat into a string :
        cat = ','.join(list_name_cat)
        return cat

    def recovers_stores(self, id_food, list_info_food):
        # Insert store into the list_info_food
        # In table store_food recover id_store_list
        store_list = self.controller.recover_store_name_list(id_food)

        if not store_list or store_list == []:
            list_info_food.insert(4, " ")
        elif len(store_list) == 1:
            list_info_food.insert(4, store_list[0])
        else:
            # recover list_name_store in String :
            store = ','.join(store_list)
            # Inserts cat  : list_info_food.insert(3, cat)
            list_info_food.insert(4, store)
        return list_info_food

    def recovers_brand(self, id_food, list_info_food):
        # Insert brand into the list_info_food
        # In brand_food table recover id_brand_list
        brand_list = self.controller.recover_brand_name_list(id_food)
        if not brand_list or brand_list == []:
            # Insert an empty string of characters to position 5
            list_info_food.insert(5, " ")
        elif len(brand_list) == 1:
            list_info_food.insert(5, brand_list[0])
        else:
            # turns the list into a string
            brand = ','.join(brand_list)
            # Insert brand in list_info_food
            list_info_food.insert(5, brand)
        return list_info_food

    def display_food_information_in_array(self, list_info_food, list_info_sub):

        list_data_col = [ARRAY_LINE_REF, list_info_food]
        if list_info_sub is not None:
            list_data_col.append(list_info_sub)
        if self.frame_info is not None:
            self.frame_info.destroy()
        self.frame_info = self.create_frame(self.frame_food, padx=10, pady=10)

        for col_number, element in enumerate(list_data_col):
            for line_number, item in enumerate(element):
                if item == "Pas de widgets text":
                    continue
                if item is None:
                    item = ""
                cell_s = scrolledtext.ScrolledText(
                    self.frame_info, bg="white", bd=2, font=("Arial", 8),
                    fg='black', width=57, height=1, wrap='word')
                cell_s.tag_config(1)

                cell = Text(self.frame_info, bg="white", bd=2,
                            font=("Arial", 8), fg='black', width=60,
                            height=1, wrap='word')
                cell.tag_config(1)
                height1 = [0, 1, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                           20]
                height2 = [2, 5, 6, 21]
                height3 = [3, 7, 8]
                if line_number in height1:
                    if len(str(item)) > 60:
                        cell_s.insert(INSERT, item, 1)
                        cell_s.grid(row=line_number, column=col_number,
                                    sticky='w')
                        cell_s.insert(INSERT, item, 1)
                        cell_s.grid(row=line_number, column=col_number,
                                    sticky='w')
                    else:
                        if col_number == 0 or line_number == 0:
                            cell.config(bg='#ADD0EC', fg='white')
                        if col_number == 0:
                            cell.config(width=40)
                        if line_number == 9 and (
                                col_number == 1 or col_number == 2):
                            if item == "contains palm oil":
                                item = "HUILE DE PALME"
                                cell.config(fg='red')
                            else:
                                item = "SANS HUILE DE PALME"
                                cell.config(fg='green')
                        cell.insert(INSERT, item, 1)
                        cell.grid(row=line_number, column=col_number,
                                  sticky='w')
                if line_number in height2:
                    cell.config(height=2)
                    cell_s.config(height=2)
                    if len(str(item)) > 120:
                        cell_s.insert(INSERT, item, 1)
                        cell_s.grid(row=line_number, column=col_number,
                                    sticky='w')
                        cell_s.insert(INSERT, item, 1)
                        cell_s.grid(row=line_number, column=col_number,
                                    sticky='w')
                    else:
                        if col_number == 0 or line_number == 0:
                            cell.config(bg='#ADD0EC', fg='white')
                        if col_number == 0:
                            cell.config(width=40)
                        cell.insert(INSERT, item, 1)
                        cell.grid(row=line_number, column=col_number,
                                  sticky='w')
                if line_number in height3:
                    cell.config(height=3)
                    cell_s.config(height=3)
                    if len(str(item)) > 180:
                        if line_number == 7 and (
                                col_number == 1 or col_number == 2):
                            cell_s.config(fg='blue')
                            cell_s.tag_bind(1, '<Button-1>',
                                            lambda e: webbrowser.open(
                                                item, new=0, autoraise=True))
                        cell_s.insert(INSERT, item, 1)
                        cell_s.grid(row=line_number, column=col_number,
                                    sticky='w')
                    else:
                        if col_number == 0 or line_number == 0:
                            cell.config(bg='#ADD0EC', fg='white')
                        if col_number == 0:
                            cell.config(width=40)
                        if line_number == 7 and (
                                col_number == 1 or col_number == 2):
                            cell.config(fg='blue')
                            cell.tag_bind(1, '<Button-1>',
                                          lambda e: webbrowser.open(
                                                item, new=0, autoraise=True))
                        cell.insert(INSERT, item, 1)
                        cell.grid(row=line_number, column=col_number,
                                  sticky='w')

        self.frame_info.grid(row=0, column=1, rowspan=20)

    def create_news_widgets(self, info_food, info_sub):
        """

        :param info_food: list
        :param info_sub: list
        """
        list_info_food = ["ALIMENT"]
        list_info_sub = ["SUBSTITUTE"]

        list_info_food.extend(info_food)
        # Insert categories into the list_info_food
        # In  category_food table recover list_id_cat
        cat = self.recovers_categories(info_food[0])
        # Insert cat in list_info_food
        list_info_food.insert(3, cat)
        # Insert store in list_info_food
        list_info_food = self.recovers_stores(info_food[0], list_info_food)
        # Insert brand in list_info_food
        list_info_food = self.recovers_brand(info_food[0], list_info_food)

        if info_sub is not None:
            list_info_sub.extend(info_sub)
            # Insert categories into the list_info_sub
            # In  category_food table recover list_id_cat
            cat = self.recovers_categories(info_sub[0])
            # Insert cat in list_info_sub
            list_info_sub.insert(3, cat)
            # Insert store in list_info_sub
            self.recovers_stores(info_sub[0], list_info_sub)
            # Insert brand in list_info_sub
            self.recovers_brand(info_sub[0], list_info_sub)
        # display_food_information in an array
        self.root.geometry("1400x620-20+20")
        self.display_food_information_in_array(list_info_food, list_info_sub)

    def save_research(self):
        # back to the controller
        self.controller.save_research(self.info_food, self.info_sub)
        self.root.geometry("450x620-20+20")
        self.back_to_the_menu()

    def see_choice_user_sub(self, event):
        selected_substitute = str(self.combo_sub.get())
        # # display substitute information
        id_food = self.controller.displays_food_information(
            selected_substitute)
        self.info_sub = self.controller.recover_info_food(id_food)
        self.create_news_widgets(self.info_food, self.info_sub)
        # Create Button Save
        self.create_button(self.frame_food, "Enregistrer", self.save_research,
                           font=("Arial", 15), row=11, sticky='e', pady=20)
        return self.selected_sub

    def see_choice_user_food(self, event):
        # get name selected food
        selected_food = str(self.combo_food.get())
        # display food information
        id_food = self.controller.displays_food_information(
            selected_food)
        self.info_food = self.controller.recover_info_food(id_food)
        print(self.info_food)
        self.create_news_widgets(self.info_food, info_sub=None)
        # display widgets for select substitute
        self.create_line(self.frame_food, 7)  # create line
        #   create label : Select a substitute
        self.label_select_sub = self.create_label(
            self.frame_food, text=" Selectionner un substitue: : ",
            fg='#ADD0EC', row=8, pady=5)

        list_sub = self.controller.substitute_research(
            nutriscore=self.info_food[2], score_nutri=self.info_food[16],
            nova=self.info_food[17])
        for substitute in list_sub:
            self.list_sub.append(substitute[1])
        # Create combobox substitute
        self.combo_sub = self.create_combobox(
            self.frame_food, self.list_sub, self.see_choice_user_sub,
            row=9, sticky='w', padx=20)

    def create_widgets(self, cat, list_food):
        """ This method creates the widgets that will be in the frame. """
        self.list_food = list_food
        # title line 1
        title_text = " BIENVENUE {} ".format(self.controller.controller.pseudo)
        self.create_label(self.frame_food, text=title_text, font=("Arial", 15),
                          fg="#ADD0EC", sticky='ns', pady=5)

        # create title line 2
        self.create_label(self.frame_food, text="RECHERCHE D'UN SUBSTITUE",
                          font=("Arial", 15), fg="#ADD0EC", row=1, pady=2)

        # Create Button Back to the menu
        self.create_button(self.frame_food, "MENU", self.back_to_the_menu,
                           font=("Arial", 14), row=1, sticky='e', pady=20)

        self.create_line(self.frame_food, 2)  # create line

        # create label category
        text_cat = " Catégorie : {}".format(cat)
        # label = master, text="text", font=("Arial", 8), bg="white",
        #         fg='black', row=0, col=0, sticky='w', padx=0, pady=0
        self.create_label(self.frame_food, text=text_cat, font=("Arial", 15),
                          fg="gray", row=3, pady=5)

        # Create Button modified category
        self.create_button(self.frame_food, "Modifier la catégorie",
                           self.back_choice_cat, font=("Arial", 12), row=4,
                           sticky='w', pady=0)

        # create subtitle : Select a food
        self.label_select_food = self.create_label(
            self.frame_food, text="Sélectionner un aliment : ", fg='#ADD0EC',
            row=5, pady=20)

        # Create combobox food
        self.combo_food = self.create_combobox(
            self.frame_food, list_food, self.see_choice_user_food,
            row=6, sticky='w', padx=20)

    def open_view_select_food(self, cat, list_food):
        """ This method opens the view """
        self.create_frame_cat()
        self.create_widgets(cat, list_food)
