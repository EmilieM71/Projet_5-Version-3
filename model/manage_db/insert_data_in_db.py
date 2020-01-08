from model.api_openfoodfacts.import_data import ImportData
from model.api_openfoodfacts.clean_data_api import CleanData
from model.tables_db.manage_tables import ManageTables
from model.manage_db.cnx_db import CnxDatabase


class InsertData:
    """ this class insert data in the database
            - create data in db
            - get info from the db matching the provided criteria. """
    cnx_db = CnxDatabase()

    def __init__(self):
        self.cnx = self.cnx_db.cnx
        self.products = []
        self.tables = ManageTables(self.cnx)

    @staticmethod
    def download_api_data(cat):
        """ Method downloads data from the Open Food Facts API """
        # Creating an object for class InsertData
        import_data = ImportData()  # Data from api
        # Recover openFoodFacts API data
        products = import_data.import_products(cat)
        # Clean data
        clean_data = CleanData()
        all_products = clean_data.clean_data(products)
        return all_products

    def insert_data_in_tables(self, products):
        # # Creating a cursor object
        cursor = self.cnx.cursor()

        # Insert data into the corresponding tables
        i=0
        for product in products:
            i+=1
            # id_food ,name ,nutriscore, url, ingredient, palm_oil,
            # allergen, energy_100g, energy, fat_100g, saturated_fat_100g,
            # carbohydrates_100g, sugars_100g, proteins_100g, salt_100g,
            # sodium_100g, nutrition_score_fr_100g, nova_group_100g
            if product["id_food"] == "" or product["name"] == "" \
                    or product["name"] is None or (
                    product["nutriscore"] == ""
                    or product["nutriscore"] is None):
                continue
            else:
                # Insert elements in food table
                self.tables.food_manager.create_food(
                    product["id_food"], product["name"], product["nutriscore"],
                    product["url"], product["ingredient"], product["palm_oil"],
                    product["allergen"], product["energy_100g"],
                    product["energy"], product["fat_100g"],
                    product["saturated_fat_100g"],
                    product["carbohydrates_100g"],
                    product["sugars_100g"], product["proteins_100g"],
                    product["salt_100g"], product["sodium_100g"],
                    product["nutrition_score_fr_100g"],
                    product["nova_group_100g"])
                id_food = product["id_food"]

                # Insert category in category table
                if product["categories"] != "" \
                        and product["categories"] is not None:
                    if product["categories"].find(",") == -1:
                        # Insert name in table category
                        id_cat = self.tables.category_manager.create_category(
                            product["categories"])
                        # Insert id_food and id_cat in cat_food table
                        self.tables.category_food_manager.\
                            search_if_cat_food_exist(id_food, id_cat)
                    else:
                        for cat in product["categories"].split(","):
                            # Search if the brand already exists in db
                            # and if not exist, insert name in table brand
                            id_cat = self.tables.category_manager.\
                                create_category(cat)
                            # Insert id_food, id_brand in food_brand table
                            self.tables.category_food_manager.\
                                search_if_cat_food_exist(id_food, id_cat)
                # Insert brand in brand table
                if product["brand"] != "" and product["brand"] is not None:
                    if product["brand"].find(",") == -1:
                        # Insert name in table brand
                        id_brand = self.tables.brand_manager.create_brand(
                            product["brand"])
                        # Insert id_food and id_brand in food_brand table
                        self.tables.food_brand_manager.\
                            search_if_food_brand_exist(id_food, id_brand)
                    else:
                        for brand in product["brand"].split(","):
                            # Search if the brand already exists in  database
                            # and if not exist, insert name in table brand
                            id_brand = self.tables.brand_manager.create_brand(
                                brand)
                            # Insert id_food and id_brand in food_brand table
                            self.tables.food_brand_manager.\
                                search_if_food_brand_exist(id_food, id_brand)

                # Insert store in store table
                if product["store"] != "" and product["store"] is not None:
                    if product["store"].find(",") == -1:
                        # Insert name in table store
                        id_store = self.tables.store_manager.create_store(
                            product["store"])
                        # Insert id_food and id_store in food_store table
                        self.tables.food_store_manager.\
                            search_if_food_store_exist(id_food, id_store)
                    else:
                        for store in product["store"].split(","):
                            # Insert name in table store
                            id_store = self.tables.store_manager.create_store(
                                store)
                            if id_store is None:
                                id_store = self.tables.store_manager.get_id(
                                    store)
                            # Insert id_food and id_store in food_store table
                            self.tables.food_store_manager.\
                                search_if_food_store_exist(id_food, id_store)

        cursor.close()

    def search_presence_api_data_in_database(self):
        """

        """
        food_table = self.tables.food_manager  # Table food
        presence_data = food_table.search_if_data()
        return presence_data

    def create(self, add, data):
        cursor = self.cnx.cursor()
        cursor.execute(add, data)
        # Make sure data is committed to the database
        self.cnx.commit()
        cursor.close()

    def filter(self, search_terms):
        """Searches objects in the database matching the provided criteria."""
        cursor = self.cnx.cursor()
        select = search_terms.get('SELECT')
        el_wanted = select.get('name_col')
        table = select.get('table')

        if 'WHERE' in search_terms:
            condition = search_terms.get('WHERE')
            conditions = " AND ".join(
                [f"{col} = {value}" for col, value in condition.items()
                 if value is not None]
            ).strip()
            conditions = f"WHERE {conditions}"
            if 'INNER JOIN' in search_terms:
                inner_join = search_terms.get('INNER JOIN')
                table_join = inner_join.get('table2')
                join_on = search_terms.get('ON')
                join_col_table1 = join_on.get('table1.col2')
                join_col_table2 = join_on.get('table2.col1')
                query = (f"SELECT {el_wanted} FROM {table} "
                         f"INNER JOIN {table_join} "
                         f"ON {join_col_table1}={join_col_table2} "
                         f"{conditions}")
            else:
                query = (f"SELECT {el_wanted} FROM {table} "
                         f"{conditions}")
            el = None
            cursor.execute(query)
            rows = cursor.fetchall()
            if not rows:
                return
            else:
                for row in rows:
                    el = row[0]
            return el


if __name__ == "__main__":
    pass
