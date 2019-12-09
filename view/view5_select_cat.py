from config import CATEGORY


class ViewSelectCat:

    def __init__(self, cont):
        self.controller = cont
        self.manage_view = cont.controller.view
        self.frame_cat = None
        self.combo = None
        self.selected_category = None

    def create_frame_cat(self):
        """ This method creates a frame in the window """
        self.frame_cat = self.manage_view.create_frame(
            self.manage_view.root, padx=5)

    def back_to_the_menu(self):
        self.controller.back_to_the_menu()

    def choice_user(self, event):
        self.selected_category = str(self.combo.get())
        return self.selected_category

    def validate_category(self):
        self.controller.get_id_selected_category(self.selected_category)

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        # title line 1
        # label = master, text="text", font=("Arial", 8), bg="white",
        #         fg='black', row=0, col=0, sticky='w', padx=0, pady=0
        title_text = " BIENVENUE {} ".format(self.controller.controller.pseudo)
        self.manage_view.create_label(self.frame_cat, text=title_text,
                                      font=("Arial", 15), fg="#ADD0EC",
                                      sticky='ns', pady=5)

        # create title line 2
        self.manage_view.create_label(self.frame_cat,
                                      text="RECHERCHE D'UN SUBSTITUE",
                                      font=("Arial", 15), fg="#ADD0EC",
                                      row=1, pady=2)

        # Create Button Back to the menu
        # Button : master, text, command, font=("Arial", 20), bg='#ADD0EC',
        #          fg='white', row=0, col=0, sticky='ns', padx=5, pady=5
        self.manage_view.create_button(self.frame_cat, "MENU",
                                       self.back_to_the_menu, row=0,
                                       sticky='e', pady=20)

        self.manage_view.create_line(self.frame_cat, 2)  # create line
        # create subtitle : Select a category:
        self.manage_view.create_label(self.frame_cat,
                                      text=" Sélectionner une catégorie : ",
                                      font=("Arial", 10), row=3, pady=20)

        # create combobox
        # Combo : (master, values_list, command, row=0, col=0,
        #                         sticky='ns', padx=5, pady=5
        self.combo = self.manage_view.create_combobox(self.frame_cat, CATEGORY,
                                                      self.choice_user, row=4,
                                                      sticky='w', padx=20)

        # Create Button validate
        self.manage_view.create_button(self.frame_cat, "VALIDER",
                                       self.validate_category,
                                       font=("Arial", 10), row=4,
                                       sticky='e', pady=20)

    def open_view_select_cat(self):
        """ This method opens the view """
        self.create_frame_cat()
        self.create_widgets()
