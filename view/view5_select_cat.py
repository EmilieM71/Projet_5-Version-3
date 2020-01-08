from view.manage_view import ManageView
from config import CATEGORY


class ViewSelectCat(ManageView):

    def __init__(self, cont):
        """

        :param cont: ControllerCategory
        """
        self.controller = cont
        self.frame_cat = None
        self.combo = None
        self.selected_category = None

    def create_frame_cat(self):
        """ This method creates a frame in the window """
        self.frame_cat = self.create_frame(self.root, padx=5)

    def back_to_the_menu(self):
        self.controller.back_to_the_menu()

    def choice_user(self, event):
        self.selected_category = str(self.combo.get())
        return self.selected_category

    def validate_category(self):
        self.frame_cat.destroy()
        self.controller.get_id_selected_category(self.selected_category)

    def create_widgets(self, pseudo):
        """ This method creates the widgets that will be in the frame. """
        # title line 1
        # label = master, text="text", font=("Arial", 8), bg="white",
        #         fg='black', row=0, col=0, sticky='w', padx=0, pady=0
        title_text = " BIENVENUE {} ".format(pseudo)
        self.create_label(self.frame_cat, text=title_text, font=("Arial", 15),
                          fg="#ADD0EC", sticky='ns', pady=5)

        self.create_label(self.frame_cat, text="RECHERCHE D'UN SUBSTITUE",
                          font=("Arial", 15), fg="#ADD0EC", row=1, pady=2)

        # Create Button Back to the menu
        self.create_button(self.frame_cat, "MENU", self.back_to_the_menu,
                           font=("Arial", 14), row=0, sticky='e', pady=20)

        self.create_line(self.frame_cat, 2)  # create line
        # create subtitle : Select a category:
        self.create_label(self.frame_cat, text="Sélectionner une catégorie : ",
                          font=("Arial", 10), row=3, pady=20)

        # create combobox
        # Combo : (master, values_list, command, row=0, col=0,
        #                         sticky='ns', padx=5, pady=5
        self.combo = self.create_combobox(self.frame_cat, CATEGORY,
                                          self.choice_user, row=4, sticky='w',
                                          padx=20)

        # Create Button validate
        self.create_button(self.frame_cat, "VALIDER", self.validate_category,
                           font=("Arial", 10), row=4, sticky='e', pady=20)

    def open_view_select_cat(self, pseudo):
        """ This method opens the view """
        self.create_frame_cat()
        self.create_widgets(pseudo)
