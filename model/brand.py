class Brand:
    """..."""

    def __init__(self, cnx):
        """Class that characterizes the 'brand' table with its iD and name
                Args:
                    cnx : connect mysql database
                    cursor : object MySQLCursor
                """
        self.cnx = cnx
        self.cursor = cnx.cursor()
        self.brand_id = None
        self.brand_name = None

    def create_brand(self, name_brand):
        """This feature allows you to create a line in the category table"""

        # 1- Create a line in the brand table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_brand = ("INSERT INTO brand (name) "
                     "VALUES (%s)"
                     "ON DUPLICATE KEY UPDATE id=id")
        # 1.2- Storage data in a variable
        data_brand = (name_brand,)
        # 1.3- Insert new category
        self.cursor.execute(add_brand, data_brand)
        self.brand_id = self.get_id(name_brand)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        return self.brand_id

    def get_id(self, name_brand):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM brand "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_brand,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.brand_id = row[0]
        return self.brand_id

    def search_if_brand_exist(self, name_brand):
        """ This function search if the brand already exists in database"""
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM brand "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_brand,))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_brand(name_brand)
        else:
            self.get_id(name_brand)
            return

    def get_name_brand(self, id_brand):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name FROM brand "
                 "WHERE id = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_brand,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.brand_name = row[0]
            return self.brand_name

    # def read_all_brand(self):
    #     read_all_sql = " SELECT * FROM brand "
    #     self.cursor = self.cnx.cursor()
    #     self.cursor.execute(read_all_sql)

    def recover_brand_name_list(self, id_food):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name FROM brand "
                 "INNER JOIN food_brand "
                 "ON brand.id = food_brand.id_brand "
                 "WHERE food_brand.id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_food,))
        rows = self.cursor.fetchall()
        list_brand = []
        if rows:
            for row in rows:
                brand = row[0]
                list_brand.append(brand)
        return list_brand
