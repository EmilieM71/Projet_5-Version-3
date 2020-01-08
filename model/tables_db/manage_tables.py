from model.tables_db.category_manager import CategoryManager
from model.tables_db.store_manager import StoreManager
from model.tables_db.brand_manager import BrandManager
from model.tables_db.food_manager import FoodManager
from model.tables_db.user_manager import UserManager
from model.tables_db.food_brand_manager import FoodBrandManager
from model.tables_db.food_store_manager import FoodStoreManager
from model.tables_db.category_food_manager import CategoryFoodManager
from model.tables_db.user_food_manager import UserFoodManager


class ManageTables:
    """ This class manages access to the database table management classes. """

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.)
        """
        self.cnx = cnx
        self._category_manager = None
        self._store_manager = None
        self._brand_manager = None
        self._food_manager = None
        self._user_manager = None
        self._food_brand_manager = None
        self._food_store_manager = None
        self._category_food_manager = None
        self._user_food_manager = None

    @property
    def category_manager(self):
        if self._category_manager is None:
            self._category_manager = CategoryManager(self.cnx)
        return self._category_manager

    @property
    def store_manager(self):
        if self._store_manager is None:
            self._store_manager = StoreManager(self.cnx)
        return self._store_manager

    def _get_brand_manager(self):
        if self._brand_manager is None:
            self._brand_manager = BrandManager(self.cnx)
        return self._brand_manager

    brand_manager = property(_get_brand_manager)

    def _get_food_manager(self):
        if self._food_manager is None:
            self._food_manager = FoodManager(self.cnx)
        return self._food_manager

    food_manager = property(_get_food_manager)

    def _get_user_manager(self):
        if self._user_manager is None:
            self._user_manager = UserManager(self.cnx)
        return self._user_manager

    user_manager = property(_get_user_manager)

    def _get_food_brand_manager(self):
        if self._food_brand_manager is None:
            self._food_brand_manager = FoodBrandManager(self.cnx)
        return self._food_brand_manager

    food_brand_manager = property(_get_food_brand_manager)

    def _get_food_store_manager(self):
        if self._food_store_manager is None:
            self._food_store_manager = FoodStoreManager(self.cnx)
        return self._food_store_manager

    food_store_manager = property(_get_food_store_manager)

    def _get_category_food_manager(self):
        if self._category_food_manager is None:
            self._category_food_manager = CategoryFoodManager(self.cnx)
        return self._category_food_manager

    category_food_manager = property(_get_category_food_manager)

    def _get_user_food_manager(self):
        if self._user_food_manager is None:
            self._user_food_manager = UserFoodManager(self.cnx)
        return self._user_food_manager

    user_food_manager = property(_get_user_food_manager)
