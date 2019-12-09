from mysql import connector
from mysql.connector import errorcode
from config import HOST, USER, PASSWORD, DB_NAME, PATH_FILE
from model.api_open_food_facts import ApiOpenFoodFacts
from model.brand import Brand
from model.category import Category
from model.category_food import CategoryFood
from model.food import Food
from model.food_brand import FoodBrand
from model.food_store import FoodStore
from model.store import Store


class ManageDb:
    """ this class manages the database
            - Connection to MySQL
            - Connect database DB_NAME if exist, elif create DB
            - Create database
            - exit connection. """

    def __init__(self):
        self.cnx = None
        # self.cursor = None
        self.products = []

    def download_api_data(self, cat):
        """ """
        # Creating an object for class ApiOpenFoodFacts
        data_api = ApiOpenFoodFacts()  # Data from api

        # Recover openFoodFacts API data
        data_api.import_products(cat)
        data_api.clean_data(data_api.products)
        self.products.append(data_api.all_products)

        return self.products

    def insert_data_in_tables(self, products):
        # # Creating a cursor object
        cursor = self.cnx.cursor()

        # Creating an object for each class
        food_table = Food(self.cnx, cursor)  # Table food
        cat_table = Category(self.cnx, cursor)  # Table category
        cat_food_table = CategoryFood(self.cnx, cursor)  # table category_food
        brand_table = Brand(self.cnx)  # table brandself.
        food_brand_table = FoodBrand(self.cnx, cursor)  # table food_brand
        store_table = Store(self.cnx, cursor)  # Table store
        food_store_table = FoodStore(self.cnx, cursor)  # Table food_store

        # Insert data into the corresponding tables

        for product in products:
            if product[0] == "" or product[1] == "" or product[1] is None:
                return
            else:
                # Insert elements in food table
                food_table.create(product[0], product[1], product[5],
                                  product[6], product[7], product[8],
                                  product[9], product[10], product[11],
                                  product[12], product[13], product[14],
                                  product[15], product[16], product[17],
                                  product[18], product[19], product[20])
                id_food = product[0]

                # Insert category in category table
                if product[2] != "" and product[2] is not None:
                    if product[2].find(",") == -1:
                        # Insert name in table brand
                        id_cat = cat_table.create_category(product[2])
                        # Insert id_food and id_brand in food_brand table
                        cat_food_table.search_if_cat_food_exist(
                            id_food, id_cat)
                    else:
                        for cat in product[2].split(","):
                            # Search if the brand already exists in  database
                            # and if not exist, insert name in table brand
                            id_cat = cat_table.create_category(cat)
                            # Insert id_food and id_brand in food_brand table
                            cat_food_table.search_if_cat_food_exist(
                                id_food, id_cat)
                # Insert brand in brand table
                if product[4] != "" and product[4] is not None:
                    if product[4].find(",") == -1:
                        # Insert name in table brand
                        id_brand = brand_table.create_brand(product[4])
                        # Insert id_food and id_brand in food_brand table
                        food_brand_table.search_if_food_brand_exist(
                            id_food, id_brand)
                    else:
                        for brand in product[4].split(","):
                            # Search if the brand already exists in  database
                            # and if not exist, insert name in table brand
                            id_brand = brand_table.create_brand(brand)
                            # Insert id_food and id_brand in food_brand table
                            food_brand_table.search_if_food_brand_exist(
                                id_food, id_brand)

                # Insert store in store table
                if product[3] != "" and product[3] is not None:
                    if product[3].find(",") == -1:
                        # Insert name in table store
                        id_store = store_table.create_store(product[3])
                        # Insert id_food and id_brand in food_brand table
                        food_store_table.search_if_food_store_exist(
                            id_food, id_store)
                    else:
                        for store in product[3].split(","):
                            # Insert name in table store
                            id_store = store_table.create_store(store)
                            # Insert id_food and id_store in food_store table
                            food_store_table.search_if_food_store_exist(
                                id_food, id_store)

        cursor.close()

    def search_presence_api_data_in_database(self):
        """

        """
        cursor = self.cnx.cursor()
        food_table = Food(self.cnx, cursor)  # Table food

        presence_data = food_table.search_if_data()
        return presence_data

    def create_db(self):
        """ Create database PurBeurre if not exist"""
        cursor = self.cnx.cursor()
        try:
            # Opening the file containing the SQL script
            sql_file = open(PATH_FILE, 'r')
            # Read file
            sql_text = sql_file.read()
            sql_stmts = sql_text.split(';')
            for s in sql_stmts:
                cursor.execute(s)
            # Graphical interface with Tkinter
            db_is_create = True  # The database is created
            # Mode console
            print("The database is created")
            # Make sure db is committed
            self.cnx.commit()

        except connector.Error as err:
            # Graphical interface with Tkinter
            db_is_create = False  # Failed creating database.
            # Mode console
            print("Failed creating database: {}".format(err))
            cursor.close()
            return db_is_create

        else:
            cursor.close()
            return db_is_create

    def connection_db(self):
        """ This method connects to the 'PurBeurre' database. """
        cursor = self.cnx.cursor()
        try:
            cursor.execute("USE {}".format(DB_NAME))
            connect_db = True  # The database exists and you are connect.

        except connector.Error:
            connect_db = False  # The 'PurBeurre' db does not existe.
            cursor.close()
            return connect_db

        else:
            cursor.close()
            return connect_db

    def connection_mysql(self):
        """ this function is responsible for connecting to mysql with the
        demo profile:
        - HOST = 'localhost'
        - USER = 'student_OC'
        - PASSWORD = '123abc'
        """

        # connection MySQL
        config = {
            'host': HOST,
            'user': USER,
            'password': PASSWORD
        }
        try:
            # connection to MySQL
            self.cnx = connector.connect(**config)

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print(err)
        else:
            return self.cnx

    def __exit__(self, cnx):
        """ """
        cnx.close()
        print("Connexion fermée")
