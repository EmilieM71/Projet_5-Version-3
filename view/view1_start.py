from view.manage_view import ManageView


class ViewStart(ManageView):
    """ This class is responsible for:
        - create the widgets in the view
        - open the 'start vue' and change it when the user's action
    """

    def __init__(self, cont):
        self.controller = cont
        self.frame_start = None
        # self.create_frame_start()
        self.widgets = []

    def create_frame_start(self):
        """ This method creates a frame in the window """
        self.frame_start = self.create_frame(self.root)

    def user_click_on_launch_button(self):
        """ This method allows events to run when the user clicks the
            'Start App' button"""
        self.frame_start.destroy()
        self.controller.shows_steps_view()

    def user_click_on_leave_button(self):
        """ This method allows events to run when the user clicks
                the 'Leave' button"""
        self.root.destroy()

    def user_click_on_ok2_button(self):
        new_text = "Vous avez créé un utilisateur de démo."
        self.widgets[2].config(text=new_text, fg='gray')
        self.widgets[3].destroy()
        self.widgets[4].destroy()
        self.widgets[5].destroy()
        self.widgets[6].destroy()
        self.widgets[7].destroy()
        # create line
        self.create_line(self.frame_start, 10)
        # create subtitle
        self.create_label(self.frame_start, font=("Arial", 15),
                          fg="#ADD0EC", row=11,
                          text=" Cliquez sur le bouton de votre choix : ")
        # create line
        self.create_line(self.frame_start, 12)
        # create button Launch app
        self.create_button(self.frame_start,
                           text=" Lancez l'application  ",
                           command=self.user_click_on_launch_button, row=13)
        # create button Leave
        self.create_button(self.frame_start, text="         Quitter        ",
                           command=self.user_click_on_leave_button, row=14)

    def user_click_on_ok1_button(self):
        """ This method changes the view when the user clicks the
        'ok' button """
        new_text = "Vous avez MySQL version 8 installée sur votre ordinateur."
        self.widgets[0].config(text=new_text, fg='gray')
        self.widgets[1].destroy()
        # create text for create user mysql for use the application
        text_info_user = "Maintenant, vous devez créer l'utilisateur démo : "
        # text="BIENVENUE", font=("Arial", 40), fg="#ADD0EC", sticky='ns'
        create_user = self.create_label(self.frame_start, text=text_info_user,
                                        row=5, pady=10)
        self.widgets.append(create_user)
        # create text : connection MySQL
        txt_create_user = "Connectez-vous à MySQL et entrez le script SQL " \
                          "suivant"
        user = self.create_label(self.frame_start, text=txt_create_user, row=6)
        self.widgets.append(user)
        # create text : statements sql for create user
        text_line1 = \
            "1  CREATE USER 'student_OC'@'localhost' IDENTIFIED BY '123abc';\n"
        text_line2 = \
            "2  GRANT ALL PRIVILEGES ON PurBeurre.* TO 'student'@'localhost';"
        sql_stmt = self.create_text(self.frame_start, row=7, bg="black",
                                    fg="white")
        sql_stmt.insert('1.0', text_line1)
        sql_stmt.insert('2.0', text_line2)
        self.widgets.append(sql_stmt)
        # create text : connection MySQL
        text_pma = """
        Et si vous souhaitez utiliser phpMyAdmin : Il faut changer la 
        méthode de chiffrement de l'utilisateur. Connectez en tant que root 
        au serveur Mysql avec l'interface en ligne de commande et tapez le 
        script ci dessous : """
        info_user = self.create_label(self.frame_start, text=text_pma, row=8)
        info_user.config(justify='left')
        self.widgets.append(info_user)
        # create text : statements sql for create user
        text_sql = "ALTER USER 'student_OC'@'localhost' IDENTIFIED WITH " \
                   "mysql_native_password BY '123abc';"
        sql_stmt2 = self.create_text(self.frame_start, row=9, bg="black",
                                     fg="white")
        sql_stmt2.insert('1.0', text_sql)
        self.widgets.append(sql_stmt2)
        # create button 'OK'
        button_ok2 = self.create_button(self.frame_start, "OK", row=10,
                                        command=self.user_click_on_ok2_button)
        self.widgets.append(button_ok2)

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        self.create_label(self.frame_start, text="BIENVENUE", fg="#ADD0EC",
                          font=("Arial", 40), sticky='ns', pady=5)  # title
        self.create_line(self.frame_start, 1)  # line
        self.create_label(self.frame_start, text="Informations : ",
                          font=("Arial", 15), fg="#ADD0EC", row=2)  # subtitle
        self.create_line(self.frame_start, 3)  # line
        # create text : information to know before launching the application
        txt_info = """\
        Pour utiliser cette application, vous devez avoir MySQL version 8 
        installé. Cliquez sur OK, si MySQL Version 8 est installée, sinon
        fermez l'application et installez MySQL"""
        info = self.create_label(self.frame_start, txt_info, row=4)
        info.config(justify='left')
        self.widgets.append(info)
        # create button "OK"
        button_ok1 = self.create_button(self.frame_start, "OK", row=5,
                                        command=self.user_click_on_ok1_button)
        self.widgets.append(button_ok1)

    def open_view_start(self):
        """ This method opens the view """
        self.create_frame_start()
        self.create_widgets()
        self.root.mainloop()

    def show_start_view_user(self):
        self.create_frame_start()
        self.widgets = []
        self.create_widgets()
        self.user_click_on_ok1_button()

    def db_is_create(self):
        self.root.geometry("450x620-20+20")
        self.user_click_on_launch_button()

    def create_db(self):
        # self.manage_view.root.geometry("1200x700-5+5")
        # frame
        frame = self.create_frame(self.root, padx=5, pady=5)
        # title in frame
        self.create_label(frame, font=("Arial", 14), fg="#ADD0EC", pady=5,
                          text="CREATION DE LA BASE DE DONNEES", sticky='ns')

        photo = self.create_photo_image(file_path="resource/Images/mdp.gif")
        can = self.create_canvas(frame, width=1400, height=632, row=1)
        self.create_x_scrollbar(frame, can)
        can.config(scrollregion=(-150, -120, photo.width()-150,
                                 photo.height()-120))
        self.canvas_create_image(can, logo=photo)

        self.create_button(frame, "Base de données 'PurBeurre' créée", row=3,
                           command=self.db_is_create, font=("Ariel", 14))
        self.root.geometry("{}x{}-5+5".format(
            int(photo.width()-400), int(photo.height())))
