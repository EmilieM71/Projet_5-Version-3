import logging
from mysql import connector
from model.tables_db.category_food import CategoryFood


class CategoryFoodManager:
    """ This class manages the interface between the category_food class
    instances and the database"""
    table = CategoryFood()

    def __init__(self, cnx):
        """ Connection with the MySQL server
            :param cnx: CMySQL.connection (Connection with the MySQL server
            can be made using the mysql.connector.connect() method or the
            mysql.connector.MySQLConnection() class.)
            """
        self.cnx = cnx

    @staticmethod
    def create_category_food_table(cursor):
        """ This method creates the category_food table in the database """
        table_description = ("CREATE TABLE category_food ("
                             "category_id INTEGER NOT NULL,"
                             "food_id VARCHAR(20) NOT NULL,"
                             "CONSTRAINT category_food_pk "
                             "PRIMARY KEY (category_id, food_id)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
                             ""
                             "ALTER TABLE category_food "
                             "ADD CONSTRAINT food_category_food_fk"
                             "FOREIGN KEY (food_id)"
                             "REFERENCES food (id_food)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;"
                             ""
                             "ALTER TABLE category_food "
                             "ADD CONSTRAINT category_category_food_fk"
                             "FOREIGN KEY (category_id)*"
                             "REFERENCES category (id_category)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;")
        try:
            logging.INFO("Creating category_food table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_category_food(self, cat_id, food_id):
        """This feature allows you to create a line in the category_food
        table"""
        cursor = self.cnx.cursor()
        # 1- Create a line in the food category_food
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_category_food = ("INSERT INTO category_food"
                             "(category_id, food_id)"
                             "VALUES (%s, %s);")
        # 1.2- Storage data in a variable
        data_category_food = (cat_id, food_id)
        # 1.3- Insert new category
        cursor.execute(add_category_food, data_category_food)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        cursor.close()
        return

    def search_if_cat_food_exist(self, food_id, cat_id):
        """ This function search if the food already exists in the database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM category_food "
                 "WHERE category_id = %s and food_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (cat_id, food_id))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            self.create_category_food(cat_id, food_id)
        else:
            cursor.close()
            return

    def recovering_list_id_food(self, cat_id):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT food_id FROM category_food "
                 "WHERE id_category = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (cat_id, ))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            print("Il n'y a aucun produit pour cette catégorie")
        else:
            list_id_food = []
            for row in rows:
                id_food = row[0]
                list_id_food.append(id_food)
            cursor.close()
            return list_id_food

    def recovering_list_id_cat(self, food_id):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT category_id FROM category_food "
                 "WHERE food_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (food_id, ))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            print("Il n'y a aucun catégorie pour cet aliment")
        else:
            list_id_cat = []
            for row in rows:
                id_cat = row[0]
                list_id_cat.append(id_cat)
            cursor.close()
            return list_id_cat
