class Store:
    """ This 'store' class of the model package contains methods for:
    - Create,
    - Read one or more data,
    - Update
    - Delete """

    def __init__(self, cnx, cursor):
        """ Class characterizes the 'store' table with its ID and name that
        each correspond to a column of that table.
                Args:
                    cnx : connect mysql database
                    cursor : object MySQLCursor
                """
        self.cnx = cnx
        self.cursor = cnx.cursor()
        self.store_id = None
        self.store_name = None

    def create_store(self, name_store):
        """This feature allows you to create a line in the store table"""

        # 1- Create a line in the store table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_store = ("INSERT INTO store (name) "
                     "VALUES (%s)"
                     "ON DUPLICATE KEY UPDATE id=id")
        # 1.2- Storage data in a variable
        data_store = (name_store,)
        # 1.3- Insert new store
        self.cursor.execute(add_store, data_store)
        self.store_id = self.get_id(name_store)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        return self.store_id

    def get_id(self, name_store):
        """ This feature characterizes the 'store' table with its ID and name
        that each correspond to a column of that table. """
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM store "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_store,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.store_id = row[0]
            return self.store_id

    def get_name_store(self, id_store):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name FROM store "
                 "WHERE id = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_store,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.store_name = row[0]
            return self.store_name

    def search_if_store_exist(self, name_store):
        """ This function search if the store already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM store "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_store,))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_store(name_store)
        else:
            self.get_id(name_store)
            return

    def recover_store_name_list(self, id_food):
        # Storage of the SELECT statement (SQL) in a variable
        #  '3017620422003'
        query = ("SELECT name FROM store "
                 "INNER JOIN food_store "
                 "ON store.id = food_store.id_store "
                 "WHERE food_store.id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_food,))
        rows = self.cursor.fetchall()
        list_store = []
        if rows:
            for row in rows:
                store = row[0]
                list_store.append(store)
        return list_store
