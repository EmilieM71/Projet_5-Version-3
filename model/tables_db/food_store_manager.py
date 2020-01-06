import logging
from mysql import connector
from model.tables_db.food_store import FoodStore


class FoodStoreManager:
    """ This class manages the interface between the food_store class instances
        and the database"""
    table = FoodStore()

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.)"""
        self.cnx = cnx

    @staticmethod
    def create_food_store_table(cursor):
        """ This method creates the food_store table in the database """
        table_description = ("CREATE TABLE food_store ("
                             "store_id INTEGER NOT NULL,"
                             "food_id VARCHAR(20) NOT NULL,"
                             "CONSTRAINT food_store_pk "
                             "PRIMARY KEY (store_id, food_id)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
                             ""
                             "ALTER TABLE food_store "
                             "ADD CONSTRAINT store_food_store_fk"
                             "FOREIGN KEY (store_id)"
                             "REFERENCES store (id_store)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;"
                             ""
                             "ALTER TABLE food_store "
                             "ADD CONSTRAINT food_food_store_fk"
                             "FOREIGN KEY (food_id)"
                             "REFERENCES food (id_food)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;")
        try:
            logging.INFO("Creating food_store table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_food_store(self, food_id, store_id):
        """This feature allows you to create a line in the category_food
        table"""
        cursor = self.cnx.cursor()
        # 1- Create a line in the food_store
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food_store = ("INSERT INTO food_store (food_id, store_id)"
                          "VALUES (%s, %s)")
        # 1.2- Storage data in a variable
        data_food_store = (food_id, store_id)
        # 1.3- Insert new food_store
        cursor.execute(add_food_store, data_food_store)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        cursor.close()

    def search_if_food_store_exist(self, food_id, store_id):
        """ This function search if the food_store already exists in the
        database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM food_store "
                 "WHERE food_id = %s and store_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (food_id, store_id))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            self.create_food_store(food_id, store_id)
        else:
            cursor.close()
            return

    def recovering_list_id_store(self, id_food):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT store_id FROM food_store "
                 "WHERE food_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        list_id_store = []
        if not rows:
            print("Il n'y a aucun magasin pour cet aliment")
            cursor.close()
        else:
            for row in rows:
                id_store = row[0]
                list_id_store.append(id_store)
            cursor.close()
        return list_id_store
