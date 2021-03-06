from view.manage_view import ManageView


class ViewWelcome(ManageView):
    """ This class displays the elements of the 'welcome' view """

    def __init__(self, cont):
        """

        :param cont: ControllerWelcome
        """
        self.controller = cont
        self.frame_welcome = None

    def create_frame_welcome(self):
        """ This method creates a frame in the window """
        self.frame_welcome = self.create_frame(self.root, padx=5)

    def find_substitute(self):
        """ This method displays the select a category view and destroys the
        frame welcome"""
        self.frame_welcome.destroy()
        self.controller.find_substitute()

    def review_substitute(self):
        """ This method displays the welcome view and destroys the
        frame welcome"""
        self.frame_welcome.destroy()
        self.controller.review_substitute()

    def exit_the_application(self):
        """ This method closes the connection to mysql and destroys the main
        application window """
        self.controller.disconnection_mysql()
        self.root.destroy()

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        # title
        title_text = " BIENVENUE {} ".format(
            self.controller.controller.info_user[1])
        self.create_label(self.frame_welcome, text=title_text,
                          font=("Arial", 15), fg="#ADD0EC", sticky='ns')
        self.create_label(self.frame_welcome,
                          text=" DANS L'APPLICATION PUR BEURRE ",
                          font=("Arial", 15), fg="#ADD0EC", row=1, sticky='ns')

        self.create_line(self.frame_welcome, 2)  # create line

        # What do you want to do?
        self.create_label(self.frame_welcome, text="Que voulez-vous faire ?",
                          font=("Arial", 15), fg="#ADD0EC", row=3, pady=20,
                          padx=20)

        #   1. Find a substitute.
        self.create_button(self.frame_welcome, "Rechercher un substitue",
                           self.find_substitute, row=4, pady=20)

        #   2. Review substitutes.
        self.create_button(self.frame_welcome, "Voir vos substitues",
                           self.review_substitute, row=5, pady=20)

        #   3. Leave
        self.create_button(self.frame_welcome, "Quitter",
                           self.exit_the_application, row=6, pady=20)

    def open_view_welcome(self):
        """ This method opens the view """
        self.create_frame_welcome()
        self.create_widgets()

