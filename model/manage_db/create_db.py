import logging
from mysql import connector
# from mysql.connector import errorcode
from config import PATH_FILE_DB, DB_NAME
from model.tables_db.manage_tables import ManageTables


class CreateDatabase:
    """ This class is responsible for the creation of the 'PureBeurre'
    database."""

    def __init__(self, cnx):
        """ Connection with the MySQL server
            :param cnx: CMySQL.connection (Connection with the MySQL server can
            be made using the mysql.connector.connect() method or the
            mysql.connector.MySQLConnection() class.)
            """
        self.cnx = cnx
        self.tables = ManageTables(cnx)

    def connection_db(self, cursor):
        """ This method connects to the 'PurBeurre' database. """
        if not cursor:
            cursor = self.cnx.cursor()
        connect_db = False
        try:
            cursor.execute("USE {}".format(DB_NAME))
            connect_db = True
            logging.INFO("You are connected to {} database".format(DB_NAME))

        except connector.Error:
            logging.ERROR("You are not connected to {} database, error : {}"
                          .format(DB_NAME, connector.Error))
        finally:
            cursor.close()
            return connect_db

    def create_database(self):
        cursor = self.cnx.cursor()
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(
                    DB_NAME))
        except connector.Error as err:
            print("Failed creating database: {}".format(err))
        else:
            self.cnx.database = DB_NAME
            self.connection_db(cursor)
            # create tables
            self.tables.category_manager.create_category_table(cursor)
            self.tables.store_manager.create_store_table(cursor)
            self.tables.brand_manager.create_brand_table(cursor)
            self.tables.food_manager.create_food_table(cursor)
            self.tables.user_manager.create_user_table(cursor)
            self.tables.food_brand_manager.create_food_brand_table(cursor)
            self.tables.food_store_manager.create_food_store_table(cursor)
            self.tables.category_food_manager.create_category_food_table(
                cursor)
            self.tables.user_food_manager.create_user_food_table(cursor)
        finally:
            cursor.close()

    def create_db_with_file(self):
        """ Create database PurBeurre if not exist"""
        cursor = self.cnx.cursor()
        create_db = False
        try:
            # Opening the file containing the SQL script
            sql_file = open(PATH_FILE_DB, 'r')
            # Read file
            sql_text = sql_file.read()
            sql_stmts = sql_text.split(';')
            for s in sql_stmts:
                cursor.execute(s)
            # Make sure db is committed
            self.cnx.commit()
            create_db = True
            logging.INFO("The {} database is created".format(DB_NAME))

        except connector.Error as err:
            logging.INFO("Failed creating database, error : {}".format(err))
            self.create_database()

        finally:
            cursor.close()
            return create_db
