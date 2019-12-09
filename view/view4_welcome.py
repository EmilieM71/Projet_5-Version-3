class ViewWelcome:

    def __init__(self, cont):
        self.controller = cont
        self.manage_view = cont.controller.view
        self.frame_welcome = None

    def create_frame_welcome(self):
        """ This method creates a frame in the window """
        self.frame_welcome = self.manage_view.create_frame(
            self.manage_view.root, padx=5)

    def find_substitute(self):
        self.controller.find_substitute()

    def review_substitute(self):
        self.controller.review_substitute()

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        # title
        title_text = " BIENVENUE {} ".format(self.controller.controller.pseudo)
        self.manage_view.create_label(self.frame_welcome, text=title_text,
                                      font=("Arial", 15), fg="#ADD0EC",
                                      sticky='ns')
        self.manage_view.create_label(self.frame_welcome,
                                      text=" DANS L'APPLICATION PUR BEURRE ",
                                      font=("Arial", 15), fg="#ADD0EC",
                                      row=1, sticky='ns')

        self.manage_view.create_line(self.frame_welcome, 2)  # create line

        # What do you want to do?
        # label : master, text="text", font=("Arial", 8), bg="white",
        # fg='black', row=0, col=0, sticky='w', padx=0, pady=0
        self.manage_view.create_label(self.frame_welcome,
                                      text="Que voulez-vous faire ?",
                                      font=("Arial", 15), fg="#ADD0EC",
                                      row=3, pady=20, padx=20)

        #   1. Find a substitute.
        # Button : master, text, command, font=("Arial", 20), bg='#ADD0EC',
        #          fg='white', row=0, col=0, sticky='ns', padx=5, pady=5
        self.manage_view.create_button(self.frame_welcome,
                                       "Rechercher un substitue",
                                       self.find_substitute, row=4, pady=20)

        #   2. Review substitutes.
        self.manage_view.create_button(self.frame_welcome,
                                       "Voir vos substitues",
                                       self.review_substitute,
                                       row=5, pady=20)

    def open_view_welcome(self):
        """ This method opens the view """
        self.create_frame_welcome()
        self.create_widgets()

