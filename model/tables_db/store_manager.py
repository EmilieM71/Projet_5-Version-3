import logging
from mysql import connector
from model.tables_db.store import Store


class StoreManager:
    """ This class manages the interface between the Store class instances
        and the database
    """
    table = Store()

    def __init__(self, cnx):
        """ Connection with the MySQL server
            :param cnx: CMySQL.connection (Connection with the MySQL server
            can be made using the mysql.connector.connect() method or the
            mysql.connector.MySQLConnection() class.)
            """

        self.cnx = cnx

    @staticmethod
    def create_store_table(cursor):
        """ This method creates the store table in the database """
        table_description = ("CREATE TABLE store ("
                             "id_store INTEGER AUTO_INCREMENT NOT NULL, "
                             "name_store VARCHAR(255) NOT NULL, "
                             "CONSTRAINT store_pk PRIMARY KEY (id_store) "
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; "
                             "CREATE UNIQUE INDEX store_idx "
                             "ON store ( name_store );")
        try:
            logging.INFO("Creating store table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_store(self, name_store):
        """This method create a line in the store table"""
        # 1.1- Create a cursor object
        cursor = self.cnx.cursor()
        # 1.2- Storage of the INSERT statement (SQL) in a variable
        add_store = ("INSERT INTO store (name_store) "
                     "VALUES (%s)"
                     "ON DUPLICATE KEY UPDATE id_store=id_store")
        # 1.3- Storage data in a variable
        data_store = (name_store,)
        # 1.4- Insert new store
        cursor.execute(add_store, data_store)
        # 1.5- Make sure data is committed
        self.cnx.commit()
        # 1.6- Recover the Id from the instance created
        self.table.store_id = self.get_id(name_store)
        # 1.7- Close cursor object
        cursor.close()
        # 1.8- Returns the ID value of the created store
        return self.table.store_id

    def get_id(self, name_store):
        """ This method characterizes the 'store' table with its ID and name
        that each correspond to a column of that table. """
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_store FROM store "
                 "WHERE name_store = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_store,))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            return
        else:
            for row in rows:
                self.table.store_id = row[0]
            cursor.close()
            return self.table.store_id

    def get_id(self, name_store):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_store FROM store "
                 "WHERE name_store = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_store,))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            return
        else:
            for row in rows:
                Store.store_name = row[0]
            return Store.store_name

    def search_if_store_exist(self, name_store):
        """ This function search if the store already exists in database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_store FROM store "
                 "WHERE name_store = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_store,))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            self.create_store(name_store)
        else:
            cursor.close()
            self.get_id(name_store)

    def recover_store_name_list(self, id_food):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        #  '3017620422003'
        query = ("SELECT name_store FROM store "
                 "INNER JOIN food_store "
                 "ON store.id_store = food_store.store_id "
                 "WHERE food_store.food_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        list_store = []
        if rows:
            for row in rows:
                store = row[0]
                list_store.append(store)
        cursor.close()
        return list_store
