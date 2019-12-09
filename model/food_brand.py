class FoodBrand:
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
        self.brand_id = None

    def create_food_brand(self, food_id, brand_id):
        """This feature allows you to create a line in the category_food
        table"""

        # 1- Create a line in the food_brand
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food_brand = ("INSERT INTO food_brand (id_food, id_brand)"
                          "VALUES (%s, %s)")
        # 1.2- Storage data in a variable
        data_food_brand = (food_id, brand_id)
        # 1.3- Insert new food_brand
        self.cursor.execute(add_food_brand, data_food_brand)
        # 1.4- Make sure data is committed
        self.cnx.commit()

    def search_if_food_brand_exist(self, food_id, brand_id):
        """ This function search if the food_brand already exists in the
        database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM food_brand "
                 "WHERE id_food = %s and id_brand = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (food_id, brand_id))
        rows = self.cursor.fetchall()
        if not rows:
            self.create_food_brand(food_id, brand_id)
        else:
            return

    def recovering_list_id_brand(self, id_food):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_brand FROM food_brand "
                 "WHERE id_food = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (id_food, ))
        rows = self.cursor.fetchall()
        list_id_brand = []
        if not rows:
            print("Il n'y a aucun marques pour cet aliment")
        else:
            for row in rows:
                id_brand = row[0]
                list_id_brand.append(id_brand)
        return list_id_brand
