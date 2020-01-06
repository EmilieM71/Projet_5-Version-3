from model.api_openfoodfacts.import_data import ImportData
from model.api_openfoodfacts.clean_data_api import CleanData


class DownloadData:

    def __init__(self):
        self.all_products = []

    def download_api_data(self, cat):
        """ Method downloads data from the Open Food Facts API """
        # Creating an object for class ApiOpenFoodFacts
        import_data = ImportData()  # Data from api
        # Recover openFoodFacts API data
        products = import_data.import_products(cat)
        # Clean data
        clean_data = CleanData()
        self.all_products = clean_data.clean_data(products)
        return self.all_products
