from tkinter import messagebox


class ViewSteps:

    def __init__(self, cont):
        self.controller = cont
        self.manage_view = cont.controller.view
        self.frame_steps = None
        self.can = None

    def create_frame_steps(self):
        """ This method creates a frame in the window """
        self.frame_steps = self.manage_view.create_frame(self.manage_view.root,
                                                         padx=5)

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        # title
        text_title = " ETAPES DE LANCEMENT DE L'APPLICATION "
        self.manage_view.create_label(self.frame_steps, text=text_title,
                                      font=("Arial", 12), fg="#ADD0EC",
                                      sticky='ns')
        self.manage_view.create_line(self.frame_steps, 1)  # create line

        # create canvas
        can = self.manage_view.create_canvas(self.frame_steps, width=430,
                                             height=500, row=2)

        can.create_rectangle((175, 10), (325, 30), width=4, outline='green')
        can.create_text((250, 20), text=" Lancement de l'application ")
        can.create_line((250, 30), (250, 45), fill='green', arrow='last',
                        width=4)
        can.create_rectangle((175, 45), (325, 65), width=4, outline='green')
        can.create_text((250, 55), text="Connexion à MySQL")
        can.create_line((250, 65), (250, 80), fill='green', arrow='last',
                        width=4)
        can.create_polygon([(200, 100), (250, 120), (300, 100), (250, 80)],
                           width=4, fill='', outline="green")
        can.create_text((250, 100), text="Connecté ?")

        return can

    def create_widgets_connect_to_mysql(self, can, cnx):
        arrow_yes_1 = can.create_line(150, 100, 200, 100, arrow='first')
        rect_yes1 = can.create_rectangle((100, 90), (150, 110))
        can.create_text((125, 100), text='OUI')
        arrow_under_yes1 = can.create_line((125, 110), (125, 125),
                                           arrow='last')
        arrow_no_1 = can.create_line((300, 100), (340, 100), arrow='last')
        rect_no1 = can.create_rectangle((340, 90), (390, 110))
        can.create_text((365, 100), text='NON')
        arrow_under_no1 = can.create_line((365, 110), (365, 125), arrow='last')
        rect_no_connect_mysql = can.create_rectangle((305, 125), (425, 200))
        can.create_text((365, 135), text="Quelque chose ne")  # 4b l1
        can.create_text((365, 153), text="va pas avec votre")  # 4b l2
        can.create_text((365, 171), text="nom d'utilisateur ou")  # 4b l3
        can.create_text((365, 189), text="votre mot de passe")  # 4b l4

        rect_connect_mysql = can.create_rectangle((50, 125), (200, 165))
        can.create_text(125, 135, text="Connection à la base de")
        can.create_text(125, 153, text="données 'Pur_Beurre'")
        arrow_under_rect_connect_mysql = can.create_line(
            (125, 165), (125, 180), arrow='last')
        # connect to database
        polygon_2 = can.create_polygon([(75, 200), (125, 220), (175, 200),
                                        (125, 180)], fill='', outline='black')
        can.create_text(125, 200, text='connecté ?')  # polygon_2
        if cnx:
            # Shows the steps in green on the flow diagram
            can.itemconfig(arrow_yes_1, fill='green', width=4)
            can.itemconfig(rect_yes1, outline='green', width=4)
            can.itemconfig(arrow_under_yes1, fill='green', width=4)
            can.itemconfig(rect_connect_mysql, outline='green', width=4)
            can.itemconfig(arrow_under_rect_connect_mysql, fill='green',
                           width=4)
            can.itemconfig(polygon_2, outline='green', width=4)
            # connect to the 'PurBeurre' database
            self.controller.connect_to_db(can)
        else:
            # Shows the steps in red on the flow diagram
            can.itemconfig(arrow_no_1, fill='red', width=4)
            can.itemconfig(rect_no1, outline='red', width=4)
            can.itemconfig(arrow_under_no1, fill='red', width=4)
            can.itemconfig(rect_no_connect_mysql, outline='red', width=4)
            # create a button for back to the start view to create a demo user
            text = "Retour vers accueil pour la création d'un utilisateur demo"
            self.manage_view.create_button(
                self.frame_steps, text, self.back_start_for_create_user,
                font=("Arial", 12), row=3)

    def back_start_for_create_user(self):
        self.frame_steps.destroy()
        self.controller.back_start_for_create_user()

    def create_widgets_connect_db(self, can, connect_db):
        arrow_yes_2 = can.create_line((60, 200), (75, 200), arrow='first')
        rect_yes2 = can.create_rectangle((10, 190), (60, 210))
        can.create_text((35, 200), state='disabled', text='OUI')
        line_under_yes2 = can.create_line((35, 210), (35, 385))
        arrow_under_yes2 = can.create_line((35, 385), (135, 385), arrow='last')
        search_presence_data_in_db = can.create_rectangle((135, 365),
                                                          (295, 405))
        can.create_text((215, 375), text='Recherche la présence de')
        can.create_text((215, 395), text="données de l'API dans la bdd")
        arrow_under_rect_presence_data = can.create_line(
            (215, 405), (215, 420), arrow='last')

        polygon_4 = can.create_polygon([(165, 440), (215, 460), (265, 440),
                                        (215, 420)], fill='', outline='black')
        can.create_text(215, 440, text='Données ?')  # polygon4

        arrow_no_2 = can.create_line((175, 200), (190, 200), arrow='last')
        rect_no2 = can.create_rectangle((190, 190), (240, 210))
        can.create_text((215, 200), state='disabled', text='NON')
        arrow_under_no2 = can.create_line((215, 210), (215, 225), arrow='last')
        rect_create_db = can.create_rectangle((170, 225), (260, 245))
        can.create_text((215, 235), text='Création bdd')
        arrow_under_rect_create_db = can.create_line((215, 245), (215, 255))
        polygon_3 = can.create_polygon([(165, 275), (215, 255), (265, 275),
                                        (215, 295)], fill='', outline='black')
        can.create_text(215, 275, text='bdd créée ?')  # polygon3
        arrow_no_3 = can.create_line((150, 275), (165, 275), arrow='first')
        rect_no3 = can.create_rectangle((100, 265), (150, 285))
        can.create_text((125, 275), state='disabled', text='NON')
        arrow_under_no3 = can.create_line((125, 285), (125, 300), arrow='last')
        failed_creation_db = can.create_rectangle((50, 300), (200, 340))
        can.create_text((125, 310), text="Échec lors de la création")
        can.create_text((125, 328), text="de la base de données.")

        arrow_yes_3 = can.create_line((265, 275), (280, 275), arrow='last')
        rect_yes3 = can.create_rectangle((280, 265), (330, 285))
        can.create_text((305, 275), text='OUI')
        line_above_yes3 = can.create_line((295, 145), (295, 265))
        arrow_under_yes3 = can.create_line((200, 145), (295, 145),
                                           arrow='first')
        if connect_db:
            # Shows the steps in green on the flow diagram
            can.itemconfig(arrow_yes_2, fill='green', width=4)
            can.itemconfig(rect_yes2, outline='green', width=4)
            can.itemconfig(line_under_yes2, fill='green', width=4)
            can.itemconfig(arrow_under_yes2, fill='green', width=4)
            can.itemconfig(search_presence_data_in_db, outline='green',
                           width=4)
            can.itemconfig(arrow_under_rect_presence_data, fill='green',
                           width=4)
            can.itemconfig(polygon_4, outline='green', width=4)
            self.controller.search_presence_api_data_in_db(can)
        else:
            # Shows the steps in green on the flow diagram
            can.itemconfig(arrow_no_2, fill='green', width=4)
            can.itemconfig(rect_no2, outline='green', width=4)
            can.itemconfig(arrow_under_no2, fill='green', width=4)
            can.itemconfig(rect_create_db, outline='green', width=4)
            can.itemconfig(arrow_under_rect_create_db, fill='green', width=4)
            can.itemconfig(polygon_3, outline='green', width=4)
            # Creating database 'Pur_Beurre'
            create_db = self.controller.create_db()
            if create_db:
                # Shows the steps in green on the flow diagram
                can.itemconfig(arrow_yes_3, fill='green', width=4)
                can.itemconfig(rect_yes3, outline='green', width=4)
                can.itemconfig(line_above_yes3, fill='green', width=4)
                can.itemconfig(arrow_under_yes3, fill='green', width=4)
                # Connection to the 'Pur_Beurre' database
                self.controller.connect_to_db(can)
            else:
                # Shows the steps in red on the flow diagram
                can.itemconfig(arrow_no_3, fill='red', width=4)
                can.itemconfig(rect_no3, outline='red', width=4)
                can.itemconfig(arrow_under_no3, fill='red', width=4)
                can.itemconfig(failed_creation_db, outline='red', width=4)
                # Open messagebox
                messagebox.showerror(
                    "Erreur lors de la création de la base de données",
                    "Vous devez créer la base de données manuellement")
                # Return view_steps
                self.frame_steps.destroy()
                self.controller.return_to_the_start_view()

    def user_click_on_login_button(self):
        self.frame_steps.destroy()
        self.controller.login()

    def user_click_on_download_button(self):
        self.controller.download_data()
        self.frame_steps.destroy()

    def create_widgets_presence_data(self, can, presence_data):
        arrow_yes_4 = can.create_line((160, 440), (175, 440), arrow='first')
        rect_yes4 = can.create_rectangle((110, 430), (160, 450))
        can.create_text((135, 440), text='OUI')
        arrow_under_yes4 = can.create_line((135, 450), (135, 465),
                                           arrow='last')
        rect_login = can.create_rectangle((100, 465), (170, 485))
        can.create_text((135, 475), text='Se connecter')
        arrow_no_4 = can.create_line((275, 440), (290, 440), arrow='last')
        rect_no4 = can.create_rectangle((290, 430), (340, 450))
        can.create_text((315, 440), text='NON')
        arrow_under_no4 = can.create_line((315, 450), (315, 460), arrow='last')
        rect_download_data = can.create_rectangle((240, 460), (390, 500))
        can.create_text((315, 470), text='Chargement des données')
        can.create_text((315, 490), text='avant connexion')
        # Search presence API data in the 'Pur_Beurre' database
        if presence_data:
            can.itemconfig(arrow_yes_4, fill='green', width=4)
            can.itemconfig(rect_yes4, outline='green', width=4)
            can.itemconfig(arrow_under_yes4, fill='green', width=4)
            can.itemconfig(rect_login, outline='green', width=4)
            text_login = "Se connecter"
            self.manage_view.create_button(
                self.frame_steps, text_login, self.user_click_on_login_button,
                font=("Arial", 12), row=3)
        else:
            can.itemconfig(arrow_no_4, fill='green', width=4)
            can.itemconfig(rect_no4, outline='green', width=4)
            can.itemconfig(arrow_under_no4, fill='green', width=4)
            can.itemconfig(rect_download_data, outline='green', width=4)
            text = "Chargement des données de l'API avant connexion"
            self.manage_view.create_button(
                self.frame_steps, text, self.user_click_on_download_button,
                font=("Arial", 12), row=3)
        # self.controller.search_presence_api_data_in_db(can)

    def open_view_steps(self):
        """ This method opens the view """
        self.create_frame_steps()
        can = self.create_widgets()
        self.controller.connect_to_mysql(can)


