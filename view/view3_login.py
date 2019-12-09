from tkinter import messagebox
import re
import hashlib


class ViewLogin:

    def __init__(self, cont):
        self.controller = cont
        self.manage_view = cont.controller.view
        self.frame_login = None
        # Entry for login
        self.message = None
        self.e_pseudo_login = None
        self.e_password_login = None
        # Entry for create an account
        self.message2 = None
        self.e_pseudo2 = None
        self.e_password2 = None
        self.info_password = None
        self.e_email = None

    def create_frame_login(self):
        """ This method creates a frame in the window """
        self.frame_login = self.manage_view.create_frame(self.manage_view.root,
                                                         padx=5)

    @staticmethod
    def b_info_password():
        messagebox.showinfo("Informations pour la création du mot de passe",
                            "Le mot de passe doit comporter au moins :\n"
                            "- une minuscule\n"
                            "- une majuscule\n"
                            "- un chiffre\n"
                            "- un caractère spéciale.\n"
                            "Il doit contenir entre 6 et 15 caractères et "
                            "aucun caractère d'espace blanc n'est autorisé.\n",
                            default='ok', icon='info')

    def function_b_login(self):
        pseudo = self.e_pseudo_login.get()
        password = self.e_password_login.get()
        password_encryption = self.password_encryption(password)

        info_user = self.controller.verify_if_user_exists(pseudo,
                                                          password_encryption)
        # If the user does not exists: displays a message indicating that the
        # user does not exists (to log in or create an account)
        if not info_user:
            self.message['text'] = "L'utilisateur n'existe pas. "
            self.message['bg'] = "#F6BABA"
            self.message['fg'] = "red"
            self.e_pseudo_login.delete(0, 255)
            self.e_password_login.delete(0, 255)

        # Else (user exist)  open view pur Beurre welcome
        else:
            self.controller.select_cat()

    @staticmethod
    def checks_email(email):
        if email == '':
            return False
        else:
            motif = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+" \
                    r"(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
            return re.match(motif, email) is not None

    @staticmethod
    def check_password(password):
        if password == '':
            return False
        else:
            motif = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]" \
                    r"{6,15}$"
            return re.match(motif, password) is not None

    @staticmethod
    def password_encryption(password2):
        password = hashlib.sha256(password2.encode())
        return password.hexdigest()

    def b_create_account(self):
        pseudo2 = self.e_pseudo2.get()
        password2 = self.e_password2.get()
        # check if the password is compliant
        check_password = self.check_password(password2)
        if not check_password:
            self.message2['text'] = "Mot de passe incorrect . "
            self.message2['bg'] = "#F6BABA"
            self.message2['fg'] = "red"
            self.e_password2.delete(0, 255)
            return
        # Hache le mot-de-passe
        password = self.password_encryption(password2)

        email = self.e_email.get()
        # check if the email is compliant
        check_email = self.checks_email(email)
        if not email or not check_email:
            self.message2['text'] = "Adresse mail incorrecte "
            self.message2['bg'] = "#F6BABA"
            self.message2['fg'] = "red"
            self.e_email.delete(0, 255)
            return
        # Check if the pseudo exists
        pseudo = self.controller.search_if_pseudo_exist(pseudo2)
        # If the user exists: displays a message indicating that the user
        # exists, and asks to choose another nickname
        if pseudo:
            self.message2['text'] = "Ce pseudo existe déjà. " \
                                    "Choississez un autre pseudo"
            self.message2['bg'] = "#F6BABA"
            self.message2['fg'] = "red"
            self.e_pseudo2.delete(0, 255)
            self.e_password2.delete(0, 255)
        # Else create a new user
        else:
            self.controller.create_user(pseudo2, password, email)

    def create_widgets(self):
        """ This method creates the widgets that will be in the frame. """
        # title
        self.manage_view.create_label(self.frame_login, text=" SE CONNECTER",
                                      font=("Arial", 12), fg="#ADD0EC",
                                      sticky='ns')
        self.manage_view.create_line(self.frame_login, 1)  # create line

        # message
        # label : master, text="text", font=("Arial", 8), bg="white",
        # fg='black', row=0, col=0, sticky='w', padx=0, pady=0
        self.message = self.manage_view.create_label(
            self.frame_login, text=None, font=("Arial", 15), row=2,
            sticky='ns', padx=20, pady=5)
        # create label Pseudo
        self.manage_view.create_label(
            self.frame_login, text=" Pseudo : ", font=("Arial", 15),
            row=3, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_pseudo_login = self.manage_view.create_entry(self.frame_login,
                                                            row=3)

        # create label Password
        self.manage_view.create_label(
            self.frame_login, text=" Mot de passe : ", font=("Arial", 15),
            row=4, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_password_login = self.manage_view.create_entry(self.frame_login,
                                                              row=4)
        self.e_password_login.confif(show='*')

        # create button LOG IN
        self.manage_view.create_button(
            self.frame_login, "Se connecter", self.function_b_login,
            font=("Arial", 15), row=5, padx=15, pady=15)

        self.manage_view.create_line(self.frame_login, 6)  # create line

        # create label New user
        self.manage_view.create_label(
            self.frame_login, text=" Nouvel utilisateur ", font=("Arial", 12),
            fg="#ADD0EC", row=7, sticky='ns')

        # message: this pseudo already exists, choose another pseudo
        self.message2 = self.manage_view.create_label(
            self.frame_login, text=None, font=("Arial", 15), row=8,
            sticky='ns', padx=20, pady=5)

        # create label Pseudo
        self.manage_view.create_label(
            self.frame_login, text=" Pseudo : ", font=("Arial", 15),
            row=9, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_pseudo2 = self.manage_view.create_entry(self.frame_login, row=9)

        # create label Password
        self.manage_view.create_label(
            self.frame_login, text=" Mot de passe : ", font=("Arial", 15),
            row=10, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_password2 = self.manage_view.create_entry(self.frame_login,
                                                         row=10)
        self.e_password2.confif(show='*')

        # create button info password
        self.info_password = self.manage_view.create_button(
            self.frame_login, " ? ", self.b_info_password, font=("Arial", 8),
            bg='gray', row=10, sticky='e')

        # create label Password
        self.manage_view.create_label(
            self.frame_login, text=" Email : ", font=("Arial", 15),
            row=11, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_email = self.manage_view.create_entry(self.frame_login, row=11)

        # create button create an account
        self.manage_view.create_button(
            self.frame_login, "Créer un compte", self.b_create_account,
            font=("Arial", 15), row=12, padx=15, pady=15)

    def open_view_login(self):
        """ This method opens the view """
        self.create_frame_login()
        self.create_widgets()
