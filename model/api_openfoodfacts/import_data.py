import requests


class ImportData:
    """class that allows you to retrieve data from the OpenFoodFact API
    in json file"""

    def __init__(self):
        self.list_1000_food_dict = []

    def import_products(self, categories):
        """
        this method is responsible of fetching products of each category.
        """
        url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        payload = {'json': 1,
                   'action': 'process',
                   'page_size': 1000,
                   'tagtype_0': 'categories',
                   'tag_contains_0': 'contains',
                   'tag_0': categories,
                   'sort_by': 'unique_scans_n'
                   }

        res = requests.get(url, payload)  # Result in json format
        # transform 'res'  into a dictionary
        # list_keys = ['products', 'page_size', 'skip', 'page', 'count']
        res_dict = res.json()

        # saves in a variable the attributes whose key is 'products'
        self.list_1000_food_dict = res_dict['products']
        return self.list_1000_food_dict


if __name__ == "__main__":
    pass
