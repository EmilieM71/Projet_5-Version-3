class ViewStart:
    """ This class is responsible for:
        - create the widgets in the view
        - open the 'start vue' and change it when the user's action
    """

    def __init__(self, cont):
        """

        :param cont: ControllerStart
        """
        self.controller = cont
        self.manage_view = cont.controller.view
        # widgets used in several methods
        self.frame_start = None
        self.widgets = []

    def create_frame_start(self):
        """ This method creates a frame in the window """
        self.frame_start = self.manage_view.create_frame(self.manage_view.root)

    def user_click_on_launch_button(self):
        """ This method allows events to run when the user clicks the
            'Start App' button"""
        self.frame_start.destroy()
        self.controller.shows_steps_view()

    def user_click_on_leave_button(self):
        """ This method allows events to run when the user clicks
                the 'Leave' button"""
        self.manage_view.root.destroy()

    def user_click_on_ok2_button(self):
        new_text = "Vous avez créé un utilisateur de démo."
        self.widgets[2].config(text=new_text, fg='gray')
        self.widgets[3].destroy()
        self.widgets[4].destroy()
        self.widgets[5].destroy()
        self.widgets[6].destroy()
        self.widgets[7].destroy()
        self.manage_view.create_line(self.frame_start, 10)  # create line
        # create subtitle
        self.manage_view.create_label(
            self.frame_start, font=("Arial", 15), fg="#ADD0EC", row=11,
            text=" Cliquez sur le bouton de votre choix : ")
        self.manage_view.create_line(self.frame_start, 12)  # create line
        # create button Launch app
        self.manage_view.create_button(
            self.frame_start, text=" Lancez l'application  ",
            command=self.user_click_on_launch_button, row=13)
        # create button Leave
        self.manage_view.create_button(
            self.frame_start, text="         Quitter        ",
            command=self.user_click_on_leave_button, row=14)

    def user_click_on_ok1_button(self):
        """ This method changes the view when the user clicks the
        'ok' button """
        new_text = "Vous avez MySQL version 8 installer sur votre ordinateur."
        self.widgets[0].config(text=new_text, fg='gray')
        self.widgets[1].destroy()
        # create text for create user mysql for use the application
        text_info_user = "Maintenant, vous devez créer l'utilisateur démo : "
        # text="BIENVENUE", font=("Arial", 40), fg="#ADD0EC", sticky='ns'
        create_user = self.manage_view.create_label(
            self.frame_start, text=text_info_user, row=5, pady=10)
        self.widgets.append(create_user)
        # create text : connection MySQL
        text_create_user = "Connectez-vous à MySQL et entrez le script SQL " \
                           "suivant"
        user = self.manage_view.create_label(
            self.frame_start, text=text_create_user, row=6)
        self.widgets.append(user)
        # create text : statements sql for create user
        text_line1 = \
            "1  CREATE USER 'student_OC'@'localhost' IDENTIFIED BY '123abc';\n"
        text_line2 = \
            "2  GRANT ALL PRIVILEGES ON PurBeurre.* TO 'student'@'localhost';"
        sql_stmt = self.manage_view.create_text(self.frame_start, row=7,
                                                bg="black", fg="white")
        sql_stmt.insert('1.0', text_line1)
        sql_stmt.insert('2.0', text_line2)
        self.widgets.append(sql_stmt)
        # create text : connection MySQL
        text_use_pma = """
        Et si vous souhaitez utiliser phpMyAdmin : Il faut changer la 
        méthode de chiffrement de l'utilisateur. Connectez en tant que root 
        au serveur Mysql avec l'interface en ligne de commande. et tapez le 
        script ci dessous : """
        info_user = self.manage_view.create_label(
            self.frame_start, text=text_use_pma, row=8)
        info_user.config(justify='left')
        self.widgets.append(info_user)
        # create text : statements sql for create user
        text_sql = "ALTER USER 'student_OC'@'localhost' IDENTIFIED WITH " \
                   "mysql_native_password BY '123abc';"
        sql_stmt2 = self.manage_view.create_text(self.frame_start, row=9,
                                                 bg="black", fg="white")
        sql_stmt2.insert('1.0', text_sql)
        self.widgets.append(sql_stmt2)
        # create button 'OK'
        button_ok2 = self.manage_view.create_button(
            self.frame_start, "OK", row=10,
            command=self.user_click_on_ok2_button)
        self.widgets.append(button_ok2)

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        # title
        self.manage_view.create_label(self.frame_start, text="BIENVENUE",
                                      font=("Arial", 40), fg="#ADD0EC",
                                      sticky='ns', pady=5)
        self.manage_view.create_line(self.frame_start, 1)
        # subtitle
        self.manage_view.create_label(self.frame_start, text="Informations : ",
                                      font=("Arial", 15), fg="#ADD0EC", row=2)
        self.manage_view.create_line(self.frame_start, 3)
        # create text : information to know before launching the application
        txt_info = """\
        Pour utiliser cette application, vous devez avoir MySQL version 8 
        installé. Cliquez sur OK, si MySQL Version 8 est installée, sinon
        fermez l'application et installez MySQL"""
        # master, text, font=("Arial", 8), bg="white", fg='black', row=0,
        # col=0, sticky='w', padx=0, pady=0)
        info = self.manage_view.create_label(self.frame_start, txt_info, row=4)
        info.config(justify='left')
        self.widgets.append(info)
        # create button "OK"
        button_ok1 = self.manage_view.create_button(
            self.frame_start, "OK", row=5,
            command=self.user_click_on_ok1_button)
        self.widgets.append(button_ok1)

    def open_view_start(self):
        """ This method opens the view """
        self.create_frame_start()
        self.create_widgets()
