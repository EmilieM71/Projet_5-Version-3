from mysql import connector
from model.tables_db.brand import Brand


class BrandManager:
    """ This class manages the interface between the Brand class instances
        and the database
    """
    brand = Brand()

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.)
        """
        self.cnx = cnx

    @staticmethod
    def create_brand_table(cursor):
        """ This method creates the brand table in the database"""
        table_description = ("CREATE TABLE brand IF NOT EXISTS("
                             "id_brand INTEGER AUTO_INCREMENT NOT NULL, "
                             "name_brand VARCHAR(255) NOT NULL, "
                             "CONSTRAINT brand_pk PRIMARY KEY (id_brand)"
                             ")ENGINE=InnoDB DEFAULT CHARSET=utf8;"
                             "CREATE UNIQUE INDEX brand_idx "
                             "ON brand ( name_brand );")
        try:
            print("Creating table brand: ", end='')
            cursor.execute(table_description)
        except connector.Error as err:
            print(err.msg)
        else:
            print("OK")

        cursor.close()

    def create_brand(self, name_brand):
        """ This method creates a line in the category table """
        # 1.1- Create a cursor object
        cursor = self.cnx.cursor()
        # 1.2- Storage of the INSERT statement (SQL) in a variable
        add_brand = ("INSERT INTO brand (name_brand) "
                     "VALUES (%s)"
                     "ON DUPLICATE KEY UPDATE id_brand=id_brand")
        # 1.3- Storage data in a variable
        data_brand = (name_brand,)
        # 1.4- Insert new category
        cursor.execute(add_brand, data_brand)
        # 1.5- Recover the Id from the instance created
        self.brand.brand_id = self.get_id(name_brand)
        # 1.6- Make sure data is committed
        self.cnx.commit()
        # 1.7- Close cursor object
        cursor.close()
        # 1.8- Returns the ID value of the created brand
        return self.brand.brand_id

    def get_id(self, name_brand):
        """ This method recovers a brand's id from its name """
        # 1.1- Create a cursor object
        cursor = self.cnx.cursor()
        # 1.2- Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_brand FROM brand "
                 "WHERE name_brand = %s")
        # 1.3- Execute SELECT statement (SQL)
        cursor.execute(query, (name_brand,))
        # 1-4-
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            return
        else:
            for row in rows:
                Brand.brand_id = row[0]
                cursor.close()
        return Brand.brand_id

    def search_if_brand_exist(self, name_brand):
        """ This function search if the brand already exists in database"""
        cursor = self.cnx.cursor()
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id_brand FROM brand "
                 "WHERE name_brand = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (name_brand,))
        rows = cursor.fetchall()
        if not rows:
            cursor.close()
            self.create_brand(name_brand)
        else:
            cursor.close()
            self.get_id(name_brand)
            return

    def get_name_brand(self, id_brand):
        # Storage of the SELECT statement (SQL) in a variable
        cursor = self.cnx.cursor()
        query = ("SELECT name_brand FROM brand "
                 "WHERE id_brand = %s")
        # Execute SELECT statement (SQL)
        cursor.execute(query, (id_brand,))
        rows = cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                Brand.brand_name = row[0]
                cursor.close()
        return Brand.brand_name

    def recover_brand_name_list(self, id_food):
        cursor = self.cnx.cursor()
        query = ("SELECT name_brand FROM brand "
                 "JOIN food_brand "
                 "ON brand.id_brand = food_brand.brand_id "
                 "WHERE food_brand.food_id = %s ")
        cursor.execute(query, (id_food,))
        rows = cursor.fetchall()
        if not rows:
            return
        else:
            list_brand_name = []
            for row in rows:
                Brand.brand_name = row[0]
                list_brand_name.append(Brand.brand_name)
                cursor.close()
            return list_brand_name
