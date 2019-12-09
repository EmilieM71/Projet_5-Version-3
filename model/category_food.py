class CategoryFood:
    """..."""

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'category_food' table with its
        id_category, id_food.

                Args:
                    cnx : connect mysql database
                """
        self.cnx = cnx
        self.cursor = cursor
        self.cat_id = None
        self.food_id = None

    def create_category_food(self, cat_id, food_id):
        """This feature allows you to create a line in the category_food
        table"""
        # 1- Create a line in the food category_food
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_category_food = ("INSERT INTO category_food"
                             "(id_category, id_food)"
                             "VALUES (%s, %s);")
        # 1.2- Storage data in a variable
        data_category_food = (cat_id, food_id)
        # 1.3- Insert new category
        self.cursor.execute(add_category_food, data_category_food)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        return

    def search_if_cat_food_exist(self, food_id, cat_id):
        """ This function search if the food already exists in the database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM category_food "
                 "WHERE id_category = %s and id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (cat_id, food_id))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_category_food(cat_id, food_id)
        else:
            return

    def recovering_list_id_food(self, cat_id):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_food FROM category_food "
                 "WHERE id_category = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (cat_id, ))
        rows = self.cursor.fetchall()
        if not rows:
            print("Il n'y a aucun produit pour cette catégorie")
        else:
            list_id_food = []
            for row in rows:
                id_food = row[0]
                list_id_food.append(id_food)
            return list_id_food

    def recovering_list_id_cat(self, food_id):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_category FROM category_food "
                 "WHERE id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (food_id, ))
        rows = self.cursor.fetchall()
        if not rows:
            print("Il n'y a aucun catégorie pour cet aliment")
        else:
            list_id_cat = []
            for row in rows:
                id_cat = row[0]
                list_id_cat.append(id_cat)
            return list_id_cat
