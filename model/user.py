class User:
    """ This 'user' class of the model package contains methods for:
           - Create,
           - Read one or more data,
           - Update
           - Delete """

    def __init__(self, cnx, cont):
        """Class that characterizes the 'user' table with its iD, email,
        pseudo and password
             :param cnx : connect mysql database
            """
        self.cnx = cnx
        if not self.cnx:
            self.cursor = None
        else:
            self.cursor = cnx.cursor()
        self.controllers = cont
        self.user_id = None
        self.email = None
        self.password = None
        self.pseudo = None

    def create_user(self, email, pseudo, password):
        """ This feature allows you to create a line in the user table"""
        # 1- Create a line in the user table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_user = ("INSERT INTO user (e_mail, pseudo, password) "
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user = (email, pseudo, password)
        # 1.3- Insert new user
        self.cursor.execute(add_user, data_user)
        self.user_id = self.cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()
        return self.user_id

    def get_id(self, pseudo, password):
        """ This method is responsible for retrieving the id of the pseudo and
         password of the user given in parameter of this one"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM user "
                 "WHERE pseudo = %s and password = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (pseudo, password))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.user_id = row[0]
                return self.user_id

    def search_if_user_exist(self, pseudo, password):
        """ This function search if the user already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM user "
                 "WHERE pseudo = %s and password = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (pseudo, password))
        rows = self.cursor.fetchall()
        if not rows:
            print("Error on pseudo or password, or account does not exist.")
            return
        else:
            self.user_id = rows[0][0]
            return self.user_id

    def search_if_pseudo_exist(self, pseudo):
        """ This function search if the user already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM user "
                 "WHERE pseudo = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (pseudo, ))
        rows = self.cursor.fetchall()
        if not rows:
            pseudo = False
            print("pseudo does not exist.")
            return pseudo
        else:
            pseudo = True
            print("Bonjour ", rows)
            return pseudo

    def save_research_substitute(self, id_user, id_sub, id_food):
        """ This feature allows you to create a line in the
        user_food_substitute table"""
        print(self.cnx)
        # 1- Create a line in the user_food_substitute table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_user_food = ("INSERT INTO user_food "
                         "(user_food, id_food, id_substitute)" 
                         "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user_food = (id_user, id_sub, id_food)
        # 1.3- Insert new user
        self.cursor.execute(add_user_food, data_user_food)
        self.user_id = self.cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()
