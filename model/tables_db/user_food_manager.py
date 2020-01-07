import logging
from mysql import connector
from model.tables_db.user_food import UserFood


class UserFoodManager:
    """ This class manages the interface between the user_food class instances
    and the database"""

    table = UserFood()

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server
        can be made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.) """
        self.cnx = cnx

    @staticmethod
    def create_user_food_table(cursor):
        """ This method creates the user_food table in the database """
        table_description = ("CREATE TABLE user_food_substitute ("
                             "food_id VARCHAR(20) NOT NULL,"
                             "substitute_id VARCHAR(20) NOT NULL,"
                             "user_id VARCHAR(255) NOT NULL,"
                             "CONSTRAINT user_food_substitute_pk "
                             "PRIMARY KEY (food_id, substitute_id, user_id)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
                             ""
                             "ALTER TABLE user_food_substitute "
                             "ADD CONSTRAINT food_user_food_substitute_fk"
                             "FOREIGN KEY (food_id)"
                             "REFERENCES food (id_food)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;"
                             ""
                             "ALTER TABLE user_food_substitute "
                             "ADD CONSTRAINT food_user_food_substitute_fk1"
                             "FOREIGN KEY (substitute_id)"
                             "REFERENCES food (id_food)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;"
                             ""
                             "ALTER TABLE user_food_substitute "
                             "ADD CONSTRAINT user_user_food_substitute_fk"
                             "FOREIGN KEY (user_id)"
                             "REFERENCES user (id_user)"
                             "ON DELETE NO ACTION"
                             "ON UPDATE NO ACTION;")
        try:
            logging.INFO("Creating category_food table : ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            logging.ERROR(err.msg)
        else:
            logging.INFO("OK")

    def create_user_food_substitute(self, user_id, food_id, substitute_id):
        """ This feature allows you to create a line in the
        user_food_substitute table"""
        cursor = self.cnx.cursor()
        # 1- Create a line in the user_food_substitute table
        # 1.1- Storage of the INSERT statement (SQL) in a variable

        add_user = ("INSERT INTO user_food_substitute "
                    "(user_id, food_id, substitute_id)"
                    "VALUES (%s, %s, %s)")
        # 1.2- Storage data in a variable
        data_user = (user_id, food_id, substitute_id)
        # 1.3- Insert new user
        cursor.execute(add_user, data_user)
        self.table.user_id = cursor.lastrowid
        # 1.4- Make sure data is committed
        self.cnx.commit()
        cursor.close()

    def search_if_research_exist(self, user_id, food_id, substitute_id):
        """ This function search if the food already exists in the database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM user_food_substitute "
                 "WHERE user_id = %s and food_id = %s and substitute_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (user_id, food_id[0], substitute_id[0]))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            self.create_user_food_substitute(user_id, food_id[0],
                                             substitute_id[0])
            return
        else:
            cursor.close()
            return rows[0]

    def search_data_in_table_for_user(self, id_user):
        """   """
        cursor = self.cnx.cursor()
        query = ("SELECT food_id, substitute_id FROM user_food_substitute "
                 "WHERE user_id = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_user,))
        rows = cursor.fetchall()
        list_food_sub = []
        if rows:
            for row in rows:
                list_food_sub.append(row)
        cursor.close()
        return list_food_sub
