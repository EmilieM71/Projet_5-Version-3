import logging
from mysql import connector
from model.tables_db.food_brand import FoodBrand


class FoodBrandManager:
    """ This class manages the interface between the food_brand class instances
        and the database"""
    table = FoodBrand()

    def __init__(self, cnx):
        """ Connection with the MySQL server
            :param cnx: CMySQL.connection (Connection with the MySQL server
            can be made using the mysql.connector.connect() method or the
            mysql.connector.MySQLConnection() class.)
            """
        self.cnx = cnx

    @staticmethod
    def create_food_brand_table(cursor):
        """ This method creates the food_brand table in the database """
        table_description = ("CREATE TABLE food_brand ("
                             "brand_id INTEGER NOT NULL,"
                             "food_id VARCHAR(20) NOT NULL,"
                             "CONSTRAINT food_brand_pk "
                             "PRIMARY KEY (brand_id, food_id)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
                             ""
                             "ALTER TABLE food_brand "
                             "ADD CONSTRAINT brand_food_brand_fk"
                             "FOREIGN KEY (brand_id)"
                             "REFERENCES brand (id_brand)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;"
                             ""
                             "ALTER TABLE food_brand "
                             "ADD CONSTRAINT food_food_brand_fk"
                             "FOREIGN KEY (food_id)"
                             "REFERENCES food (id_food)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;")
        try:
            logging.INFO("Creating food_brand table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_food_brand(self, food_id, brand_id):
        """This feature allows you to create a line in the category_food
        table"""
        cursor = self.cnx.cursor()
        # 1- Create a line in the food_brand
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food_brand = ("INSERT INTO food_brand (food_id, brand_id)"
                          "VALUES (%s, %s)")
        # 1.2- Storage data in a variable
        data_food_brand = (food_id, brand_id)
        # 1.3- Insert new food_brand
        cursor.execute(add_food_brand, data_food_brand)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        cursor.close()

    def search_if_food_brand_exist(self, food_id, brand_id):
        """ This function search if the food_brand already exists in the
        database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM food_brand "
                 "WHERE food_id = %s and brand_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (food_id, brand_id))
        rows = cursor.fetchall()
        if not rows:
            self.create_food_brand(food_id, brand_id)
        else:
            return

    def recovering_list_id_brand(self, id_food):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variabl
        query = ("SELECT brand_id FROM food_brand "
                 "WHERE food_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        list_id_brand = []
        if not rows:
            print("Il n'y a aucune marques pour cet aliment")
        else:
            for row in rows:
                id_brand = row[0]
                list_id_brand.append(id_brand)
        return list_id_brand
