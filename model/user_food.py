class UserFood:
    """ This 'UserFoodSubstitute' class of the model package contains methods
        for:
           - Create,
           - Read one or more data,
           - Update
           - Delete """

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'user' table with its iD, email,
        pseudo and password

            Args:
                cnx : connect mysql database
                cursor : object MySQLCursor
            """
        self.cnx = cnx
        self.cursor = cursor
        self.user_id = None
        self.food_id = None
        self.substitute_id = None

    def create_user_food_substitute(self, user_id, food_id, substitute_id):
        """ This feature allows you to create a line in the
        user_food_substitute table"""
        # 1- Create a line in the user_food_substitute table
        # 1.1- Storage of the INSERT statement (SQL) in a variable

        add_user = ("INSERT INTO user_food_substitute "
                    "(id_user, id_food, id_substitute)"
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user = (user_id, food_id, substitute_id)
        # 1.3- Insert new user
        self.cursor.execute(add_user, data_user)
        self.user_id = self.cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def search_if_research_exist(self, user_id, food_id, substitute_id):
        """ This function search if the food already exists in the database"""
        print(self.cnx)
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM user_food_substitute "
                 "WHERE id_user = %s and id_food = %s and id_substitute = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (user_id, food_id, substitute_id))
        rows = cursor.fetchall()
        if not rows:
            self.create_user_food_substitute(user_id, food_id, substitute_id)
            return
        else:
            cursor.close()
            return rows[0]

    def search_data_in_table_for_user(self, id_user):
        """   """
        query = ("SELECT id_food, id_substitute FROM user_food_substitute "
                 "WHERE id_user = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_user,))
        rows = self.cursor.fetchall()
        list_food_sub = []
        if rows:
            for row in rows:
                list_food_sub.append(row)
        return list_food_sub
