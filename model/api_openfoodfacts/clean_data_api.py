import re


class CleanData:
    """ This class cleans up data downloaded from the OpenFoodFacts API """

    def __init__(self):
        self.all_products = []

    @staticmethod
    def deletion_of_duplicates(string_el):
        """ This method removes duplicates """
        # Transforming the string into a list
        list_el = string_el.split(',')
        # suppression of duplicates
        new_list = set(list_el)
        # transforming the new list into a string
        new_string = ', '.join(new_list)
        return new_string

    @staticmethod
    def add_name_in_food_dict(food_dict, food):
        """ This method add name in food_dict """
        # Add 'name' value in the food dictionary
        name = food_dict.get("product_name_fr", None)
        if name is None or name == "":
            name = food_dict.get('generic_name_fr', None)
        if name is None or name == "":
            name = food_dict.get('product_name', None)
        if name is None or name == "":
            name = food_dict.get('generic_name', None)
        if name is not None:
            regex = re.compile(r'[\n\r\t]')
            name = regex.sub(" ", name)
        quantity = food_dict.get('quantity')
        if name is None:
            name = "?"
        if quantity:
            food["name"] = name + " - " + quantity
        else:
            food["name"] = name
        if name is None:
            print("pas de nom")
        return food

    @staticmethod
    def check_palm_oil_and_add_food_dict(food):
        """ This method check presence of palm oil and add palm_oil in
        food_dict """
        # check for palm oil and add 'palm_oil' value in the food dict
        if food["ingredient"] is not None:
            palm = food["ingredient"].find("palm")
            if palm > -1:
                food["palm_oil"] = "peut contenir de l'huile de palme"
            else:
                food["palm_oil"] = "Non"
        else:
            food["palm_oil"] = "peut contenir de l'huile de palme"

        return food

    @staticmethod
    def research_and_add_nutritional_information(food_dict, food):
        """ This method research and add nutritional_information in
        food_dict """
        nutritional_info = food_dict.get('nutriments', None)
        if nutritional_info is not None:
            food["energy_100g"] = nutritional_info.get('energy_100g', None)
            food["energy"] = nutritional_info.get('energy_value', None)
            food["fat_100g"] = nutritional_info.get('fat_100g', None)
            food["saturated_fat_100g"] = nutritional_info.get(
                'saturated-fat_100g', None)
            food["carbohydrates_100g"] = nutritional_info.get(
                'carbohydrates_100g', None)
            food["sugars_100g"] = nutritional_info.get('sugars_100g', None)
            food["proteins_100g"] = nutritional_info.get('proteins_100g',
                                                         None)
            food["salt_100g"] = nutritional_info.get('salt_100g', None)
            food["sodium_100g"] = nutritional_info.get('sodium_100g', None)
            food["nutrition_score_fr_100g"] = nutritional_info.get(
                'nutrition-score-fr_100g', None)
            food["nova_group_100g"] = nutritional_info.get(
                'nova-group_100g', None)
        else:
            food["energy_100g"] = None
            food["energy"] = None
            food["fat_100g"] = None
            food["saturated_fat_100g"] = None
            food["carbohydrates_100g"] = None
            food["sugars_100g"] = None
            food["proteins_100g"] = None
            food["salt_100g"] = None
            food["sodium_100g"] = None
            food["nutrition_score_fr_100g"] = None
            food["nova_group_100g"] = None
        return food

    def clean_data(self, list_1000_food_dict):
        """
        this method is responsible of making a clean data set out of the data.
        """
        for food_dict in list_1000_food_dict:
            food = {"id_food": food_dict.get("code", None),
                    "categories": food_dict.get("categories", None),
                    "store": food_dict.get("stores", None),
                    "brand": food_dict.get("brands", None),
                    "nutriscore": food_dict.get("nutrition_grade_fr", None),
                    "url": food_dict.get("url", None),
                    "ingredient": food_dict.get("ingredients_text_fr", None)}
            # Add 'name' value in the food dictionary
            food = self.add_name_in_food_dict(food_dict, food)

            # check for palm oil and add 'palm_oil' value in the food dict
            food = self.check_palm_oil_and_add_food_dict(food)

            # research the presence of allergen and add in the food dict
            all_allergen = food_dict.get('allergens_from_ingredients', None)
            if all_allergen:
                # deletion of duplicates in allergen
                food["allergen"] = self.deletion_of_duplicates(all_allergen)
            else:
                food["allergen"] = None

            # research and add nutritional information in food_dict
            food = self.research_and_add_nutritional_information(food_dict,
                                                                 food)

            # If the value is an empty string then we transform it into None
            for key, value in food.items():
                if value == "":
                    food[key] = None

            self.all_products.append(food)
        return self.all_products


if __name__ == "__main__":
    pass
