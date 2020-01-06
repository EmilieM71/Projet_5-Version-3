class FoodBrand:
    """ This class representing the many-to-many association between
    the food and brand table"""

    def __init__(self):
        """ attributes represent the data from the food_brand table:
        - brand_id
        - food_id """
        self.brand_id = None
        self.food_id = None


