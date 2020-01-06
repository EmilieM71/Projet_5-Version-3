import logging
from mysql import connector
from model.tables_db.category import Category


class CategoryManager:
    """ This class manages the interface between the Category class instances
        and the database """

    table = Category()

    def __init__(self, cnx):
        """Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.) """
        self.cnx = cnx

    @staticmethod
    def create_category_table(cursor):
        """ This method creates the category table in the database """
        table_description = ("CREATE TABLE category ("
                             "id_cat INTEGER AUTO_INCREMENT NOT NULL, "
                             "name_cat VARCHAR(255) NOT NULL, "
                             "CONSTRAINT category_pk PRIMARY KEY (id_cat)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; "
                             "CREATE UNIQUE INDEX category_idx"
                             "ON category ( name_cat );")
        try:
            logging.INFO("Creating category table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_category(self, name_cat):
        """This feature allows you to create a line in the category table"""
        # 1.1- Create a cursor object
        cursor = self.cnx.cursor()
        # 1.2- Storage of the INSERT statement (SQL) in a variable
        add_category = ("INSERT INTO `category` (`name_cat`) "
                        "VALUES (%s) "
                        "ON DUPLICATE KEY UPDATE id_cat=id_cat;")
        # 1.3- Storage data in a variable
        data_category = (name_cat, )
        # 1.4- Insert new category
        cursor.execute(add_category, data_category)
        # 1.5- Recover the Id from the instance created
        self.table.category_id = cursor.lastrowid
        if self.table.category_id == 0:
            self.table.category_id = self.get_id(name_cat)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        # 1.7- Close cursor object
        cursor.close()
        # 1.8- Returns the ID value of the created category
        return self.table.category_id

    def get_name(self, id_cat):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT name_cat FROM category "
                 "WHERE id_cat = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_cat,))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            return
        else:
            for row in rows:
                self.table.category_name = row[0]
            cursor.close()
            return self.table.category_name

    def get_id(self, name_cat):
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_cat FROM category "
                 "WHERE name_cat = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_cat,))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            return
        else:
            for row in rows:
                self.table.category_id = row[0]
            cursor.close()
            return self.table.category_id

    def search_if_category_exist(self, name_cat):
        """ This function search if the category already exists in database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_cat FROM category "
                 "WHERE name_cat = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_cat, ))
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            self.create_category(name_cat)
        else:
            self.get_id(name_cat)
