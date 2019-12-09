class FoodStore:
    """..."""

    def __init__(self, cnx, cursor):
        """Class that characterizes the 'category_food' table with its
        id_category, id_food.

                Args:
                    cnx : connect mysql database
                """
        self.cnx = cnx
        self.cursor = cursor
        self.food_id = None
        self.store_id = None

    def create_food_store(self, food_id, store_id):
        """This feature allows you to create a line in the category_food
        table"""

        # 1- Create a line in the food_store
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food_store = ("INSERT INTO food_store (id_food, id_store)"
                          "VALUES (%s, %s)")
        # 1.2- Storage data in a variable
        data_food_store = (food_id, store_id)
        # 1.3- Insert new food_store
        self.cursor.execute(add_food_store, data_food_store)
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def search_if_food_store_exist(self, food_id, store_id):
        """ This function search if the food_store already exists in the
        database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM food_store "
                 "WHERE id_food = %s and id_store = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (food_id, store_id))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_food_store(food_id, store_id)
        else:
            return

    def recovering_list_id_store(self, id_food):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_store FROM food_store "
                 "WHERE id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_food, ))
        rows = self.cursor.fetchall()
        list_id_store = []
        if not rows:
            print("Il n'y a aucun magasin pour cet aliment")
        else:
            for row in rows:
                id_store = row[0]
                list_id_store.append(id_store)
        return list_id_store
