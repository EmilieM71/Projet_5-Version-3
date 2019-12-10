class Category:
    """..."""

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'category' table with its iD, name and
        associated number

                Args:
                    cnx : connect mysql database
                    cursor : object MySQLCursor
                """
        self.cnx = cnx
        self.cursor = cursor
        self.category_id = None
        self.name = None

    def create_category(self, name_cat):
        """This feature allows you to create a line in the category table"""

        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        # INSERT INTO `category` (`id`, `name`) VALUES (NULL, '')
        add_category = ("INSERT INTO `category` (`name`) "
                        "VALUES (%s) "
                        "ON DUPLICATE KEY UPDATE id=id;")
        # 1.2- Storage data in a variable
        data_category = (name_cat, )
        # 1.3- Insert new category
        self.cursor.execute(add_category, data_category)
        self.category_id = self.cursor.lastrowid
        if self.category_id == 0:
            self.category_id = self.get_id(name_cat)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        return self.category_id

    def get_name(self, id_cat):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name FROM category "
                 "WHERE id = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_cat,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.name = row[0]
            return self.name

    def get_id(self, name_cat):
        self.cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM category "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_cat,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.category_id = row[0]
                return self.category_id

    def search_if_category_exist(self, name_cat):
        """ This function search if the category already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM category "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_cat, ))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_category(name_cat)
        else:
            self.get_id(name_cat)
            return
