import requests
import re


class ApiOpenFoodFacts:
    """class that allows you to retrieve data from the OpenFoodFact API
    in json file"""

    def __init__(self):
        self.products = []
        self.all_products = []
        self.food = []

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
        response = requests.get(url, payload)
        response_json = response.json()
        category = response_json
        # category.keys(['products', 'page_size', 'skip', 'page', 'count'])

        self.products = category['products']
        return self.products

    def clean_data(self, products):
        """
        this method is responsible of making a clean dataset out of the data.
        """
        # keys  = ['code', 'product_name_fr', 'category', 'stores', 'brand',
        #          'url', 'nutrition_grade_fr']

        for element in products:
            id_food = element.get('code', None)
            name = element.get('generic_name_fr', None)
            if name is None or name == "":
                name = element.get('generic_name', None)
            if name is None or name == "":
                name = element.get('product_name_fr', None)
            if name is None or name == "":
                name = element.get('product_name', None)
            if name is not None:
                regex = re.compile(r'[\n\r\t]')
                name = regex.sub(" ", name)
            categories = element.get('categories', None)
            store = element.get('stores', None)
            brand = element.get('brands', None)
            nutriscore = element.get('nutrition_grade_fr', None)
            if nutriscore == "":
                nutriscore = None
            url = element.get('url', None)
            ingredient = element.get('ingredients_text_fr', None)
            if ingredient is None:
                ingredient = element.get('ingredients_text_with_allergens',
                                         None)
            if ingredient == "":
                ingredient = None
            palm_oil = None
            if ingredient is not None:
                palm = ingredient.find("palm")
                if palm > -1:
                    palm_oil = "contains palm oil"
            ingredient_with_allergen = element.get(
                'ingredients_text_with_allergens', None)
            allergen = None
            if ingredient_with_allergen is not None:
                if ingredient_with_allergen != "":
                    # Search for allergen number
                    counter = 0
                    for letter in ingredient_with_allergen:
                        if letter == "<":
                            counter += 1
                    number_allergen = int(counter / 2)
                    if number_allergen != 0:
                        index = 0
                        list_allergen = []
                        for loop in range(number_allergen):
                            start = ingredient_with_allergen.find(
                                "<span class=\"allergen\">", index)
                            end = ingredient_with_allergen.find("</span>", index)
                            name_aller = ingredient_with_allergen[start + 23:end]
                            list_allergen.append(name_aller)
                            index = end + 6
                        allergen = list_allergen[0]
                    else:
                        allergen = ''

            x = element.get('nutriments', None)
            if x is None and x != "":
                energy_100g = None
                energy = None
                fat_100g = None
                saturated_fat_100g = None
                carbohydrates_100g = None
                sugars_100g = None
                proteins_100g = None
                salt_100g = None
                sodium_100g = None
            else:
                energy_100g = x.get('energy_100g', None)
                if energy_100g is not None:
                    energy_100g = str(x.get('energy_100g')) + "kj"
                energy = x.get('energy_value', None)
                if energy is not None:
                    energy = str(x.get('energy_value')) + "kcal"
                fat_100g = x.get('fat_100g', None)
                if fat_100g is not None:
                    fat_100g = str(x.get('fat_100g')) + "g"
                saturated_fat_100g = x.get('saturated-fat_100g', None)
                if saturated_fat_100g is not None:
                    saturated_fat_100g = str(x.get('saturated-fat_100g')) + "g"
                carbohydrates_100g = x.get('carbohydrates_100g', None)
                if carbohydrates_100g is not None:
                    carbohydrates_100g = str(x.get('carbohydrates_100g')) + "g"
                sugars_100g = x.get('sugars_100g', None)
                if sugars_100g is not None:
                    sugars_100g = str(x.get('sugars_100g', None)) + "g"
                proteins_100g = x.get('proteins_100g', None)
                if proteins_100g is not None:
                    proteins_100g = str(x.get('proteins_100g', None)) + "g"
                salt_100g = x.get('salt_100g', None)
                if salt_100g is not None:
                    salt_100g = str(x.get('salt_100g', None)) + "g"
                sodium_100g = x.get('sodium_100g', None)
                if sodium_100g is not None:
                    sodium_100g = str(x.get('sodium_100g', None)) + "g"
            nutrition_score_fr_100g = x.get('nutrition-score-fr_100g', None)
            nova_group_100g = x.get('nova-group_100g', None)

            product = [id_food, name, categories, store, brand, nutriscore,
                       url, ingredient, palm_oil, allergen, energy_100g,
                       energy, fat_100g, saturated_fat_100g,
                       carbohydrates_100g, sugars_100g, proteins_100g,
                       salt_100g, sodium_100g, nutrition_score_fr_100g,
                       nova_group_100g]
            self.all_products.append(product)
        return self.all_products
