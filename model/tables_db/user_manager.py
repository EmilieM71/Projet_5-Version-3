import logging
from mysql import connector
from model.tables_db.user import User


class UserManager:
    """ This class manages the interface between the user class instances
        and the database
        """
    table = User()

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.)
        """
        self.cnx = cnx

    @staticmethod
    def create_user_table(cursor):
        """ This method creates the user table in the database """
        table_description = ("CREATE TABLE user ("
                             "id_user INTEGER AUTO_INCREMENT NOT NULL,"
                             "pseudo VARCHAR(255) NOT NULL,"
                             "e_mail VARCHAR(255) NOT NULL,"
                             "password VARCHAR(255) NOT NULL,"
                             "CONSTRAINT user_pk PRIMARY KEY (id_user)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
                             "CREATE UNIQUE INDEX user_idx"
                             "ON user ( pseudo );")
        try:
            logging.INFO("Creating user table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_user(self, email, pseudo, password):
        """ This feature allows you to create a line in the user table"""
        cursor = self.cnx.cursor()
        # 1- Create a line in the user table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_user = ("INSERT INTO user (e_mail, pseudo, password) "
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user = (email, pseudo, password)
        # 1.3- Insert new user
        cursor.execute(add_user, data_user)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        cursor.close()
        self.table.id_user = self.get_id_user(pseudo, password)
        return self.table.id_user

    def get_id_user(self, pseudo, password):
        cursor = self.cnx.cursor()
        query = ("SELECT id_user FROM user "
                 "WHERE pseudo = %s and password = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (pseudo, password))
        rows = cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.table.id_food = str(row[0])
        cursor.close()
        return self.table.id_food

    def search_if_pseudo_exist(self, pseudo):
        """ This function search if the user already exists in database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM user "
                 "WHERE pseudo = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (pseudo, ))
        rows = cursor.fetchall()
        if not rows:
            pseudo = False
            print("pseudo does not exist.")
        else:
            pseudo = True
            print("Bonjour ", rows)
        cursor.close()
        return pseudo

    def search_if_user_exist(self, pseudo, password):
        """ This function search if the user already exists in database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_user FROM user "
                 "WHERE pseudo = %s and password = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (pseudo, password))
        rows = cursor.fetchall()
        if not rows:
            print("user does not exist.")
        else:
            self.table.id_user = rows[0][0]
        cursor.close()
        return self.table.id_user

    def save_research_substitute(self, pseudo, id_sub, id_food):
        """ This feature allows you to create a line in the
        user_food_substitute table"""
        cursor = self.cnx.cursor()
        # 1- Create a line in the user_food_substitute table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_user_food = ("INSERT INTO user_food_substitute "
                         "(pseudo, id_food, id_substitute)" 
                         "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user_food = (pseudo, id_sub, id_food)
        # 1.3- Insert new user
        cursor.execute(add_user_food, data_user_food)
        # 1.4- Make sure data is committed
        self.cnx.commit()
        cursor.close()
