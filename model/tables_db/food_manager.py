import logging
from model.tables_db.food import Food
from mysql import connector
from config import DB_NAME


class FoodManager:
    """
    This class manages the interface between the Food class instances
    and the database
    """
    table = Food()

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.)
        """
        self.cnx = cnx

    @staticmethod
    def create_food_table(cursor):
        """ This method creates the food table in the database"""
        table_description = ("CREATE TABLE food ( "
                             "id_food VARCHAR(20) NOT NULL,"
                             "name_food VARCHAR(500) NOT NULL,"
                             "nutriscore VARCHAR(1) NOT NULL,"
                             "url VARCHAR(255),"
                             "ingredient VARCHAR(2000),"
                             "palm_oil VARCHAR(100),"
                             "allergen VARCHAR(1000),"
                             "energy_100g VARCHAR(10),"
                             "energy VARCHAR(10),"
                             "fat_100g VARCHAR(10),"
                             "saturated_fat_100g VARCHAR(10),"
                             "carbohydrates_100g VARCHAR(10),"
                             "sugars_100g VARCHAR(10),"
                             "proteins_100g VARCHAR(10),"
                             "salt_100g VARCHAR(100),"
                             "sodium_100g VARCHAR(100),"
                             "nutrition_score_fr_100g SMALLINT,"
                             "nova_group_100g SMALLINT,"
                             "CONSTRAINT food_pk PRIMARY KEY (id_food)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
        try:
            logging.INFO("Creating food table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_food(self, id_food, name_food, nutriscore_food, url_food,
                    ingredient, palm_oil, allergen, energy_100g, energy,
                    fat_100g, saturated_fat_100g, carbohydrates_100g,
                    sugars_100g, proteins_100g, salt_100g, sodium_100g,
                    nutrition_score_fr_100g, nova_group_100g):
        """This feature allows you to create a line in the food table and
        returns the code
        :param id_food: str
        :param name_food: str
        :param nutriscore_food: str
        :param url_food: str
        :param ingredient: str
        :param palm_oil: str
        :param allergen: str
        :param energy_100g: str
        :param energy: str
        :param fat_100g: str
        :param saturated_fat_100g: str
        :param carbohydrates_100g: str
        :param sugars_100g: str
        :param proteins_100g: str
        :param salt_100g: str
        :param sodium_100g: str
        :param nutrition_score_fr_100g: int
        :param nova_group_100g: int
        """
        # product = [id:0, name:1, nutriscore:5, url:6,
        #  ingredient:7, palm_oil:8, allergen:9, energy_100g:10,
        # energy:11, fat_100g:12, saturated_fat_100g:13,
        # carbohydrates_100g:14, sugars_100g:15, proteins_100g:16,
        # salt_100g:17, sodium_100g:18, nutrition_score_fr_100g:19,
        # nova_group_100g:20]
        cursor = self.cnx.cursor()
        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food = ("INSERT INTO food "
                    "(id_food, name_food, nutriscore, url, ingredient, "
                    "palm_oil, allergen, energy_100g, energy, fat_100g, "
                    "saturated_fat_100g, carbohydrates_100g, sugars_100g, "
                    "proteins_100g, salt_100g, sodium_100g, "
                    "nutrition_score_fr_100g, nova_group_100g)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
                    "%s, %s, %s, %s, %s, %s)"
                    "ON DUPLICATE KEY UPDATE id_food=id_food")
        # 1.2- Storage data in a variable
        data_food = (id_food, name_food, nutriscore_food, url_food,
                     ingredient, palm_oil, allergen, energy_100g, energy,
                     fat_100g, saturated_fat_100g, carbohydrates_100g,
                     sugars_100g, proteins_100g, salt_100g, sodium_100g,
                     nutrition_score_fr_100g, nova_group_100g)

        # 1.3- Insert new category
        cursor.execute(add_food, data_food)

        self.table.id_food = cursor.lastrowid
        self.cnx.commit()
        cursor.close()

    def search_if_data(self):
        """   """
        self.cnx.database = DB_NAME
        cursor = self.cnx.cursor()
        query = "SELECT id_food FROM food "
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            cursor.close()
            # Graphical interface with Tkinter
            presence_data = False  # There is no data in database
            # Mode console
            # print("There is no data in database")
            return presence_data
        else:
            # Graphical interface with Tkinter
            presence_data = True  # There is data in database
            cursor.close()

        return presence_data

    def get_id(self, name_food):
        """ This method searches for the id of the food from its name"""
        # Storage of the SELECT statement (SQL) in a variable
        cursor = self.cnx.cursor()
        query = ("SELECT id_food FROM food "
                 "WHERE name_food = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_food,))
        rows = cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.table.id_food = str(row[0])
        cursor.close()
        return self.table.id_food

    def get_name(self, id_food):
        """ This method searches for the name of the food from its id"""
        # Storage of the SELECT statement (SQL) in a variable
        cursor = self.cnx.cursor()
        query = ("SELECT name_food FROM food "
                 "WHERE id_food = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.table.name = str(row[0])
        cursor.close()
        return self.table.name

    def search_if_food_exist(self, code):
        """ This function search if the food already exists in the database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM food "
                 "WHERE id_food = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (code,))
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            return
        else:
            return rows[0]

    def recover_list_food_name_from_list_id_food(self, list_id_food):
        cursor = self.cnx.cursor()
        list_name_food = []
        for id_food in list_id_food:
            # Storage of the SELECT statement (SQL) in a variable
            query = ("SELECT name_food FROM food "
                     "WHERE id_food = %s")
            # Execute SELECT statement (SQL)
            cursor.execute(query, (id_food,))
            rows = cursor.fetchall()
            list_name_food.append(rows[0][0])
        cursor.close()
        return list_name_food

    def substitute_research(self, id_cat, nutriscore, score_nutri, nova):
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM food "
                 "INNER JOIN category_food "
                 "ON food.id_food = category_food.food_id "
                 "WHERE category_food.category_id = %s and "
                 "(`nutriscore`<= %s and `nutriscore` IS NOT NULL) and "
                 "(`nutrition_score_fr_100g` <= %s and"
                 " `nutrition_score_fr_100g` IS NOT NULL) and "
                 "(`nova_group_100g` <= %s and `nova_group_100g` IS NOT NULL) "
                 "ORDER BY `nutriscore` ASC, `nutrition_score_fr_100g` ASC, "
                 "`nova_group_100g` ASC")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_cat, nutriscore, score_nutri, nova))
        rows = cursor.fetchall()
        list_sub = []
        if rows:
            for row in rows:
                list_sub.append(row)
        cursor.close()
        return list_sub

    def recover_food_name_list(self, id_cat):
        # Storage of the SELECT statement (SQL) in a variable
        cursor = self.cnx.cursor()
        query = ("SELECT name_food FROM food "
                 "INNER JOIN category_food "
                 "ON food.id_food = category_food.food_id "
                 "WHERE category_food.category_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_cat,))
        rows = cursor.fetchall()
        list_food = []
        if rows:
            for row in rows:
                food = row[0]
                list_food.append(food)
        cursor.close()
        return list_food

    def recover_info_food(self, id_food):
        # Storage of the SELECT statement (SQL) in a variable
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM food "
                 "WHERE id_food = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        info_food = rows[0]
        return info_food

    def recover_id_cat_list(self, id_food):
        # Storage of the SELECT statement (SQL) in a variable
        cursor = self.cnx.cursor()
        query = ("SELECT category_id FROM category_food "
                 "WHERE food_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        list_id_cat = []
        if rows:
            for row in rows:
                id_cat = row[0]
                list_id_cat.append(id_cat)
        cursor.close()
        return list_id_cat

    def save_research(self, pseudo, id_food, id_sub):
        cursor = self.cnx.cursor()
        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food = ("INSERT INTO user_food_substitute "
                    "(id_food, id_substitute, pseudo)"
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_food = (pseudo, id_food, id_sub)

        # 1.3- Insert new category
        cursor.execute(add_food, data_food)

        self.table.id_food = cursor.lastrowid
        self.cnx.commit()


if __name__ == "__main__":
    pass
