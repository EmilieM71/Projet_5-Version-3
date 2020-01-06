class CategoryFood:
    """ This class representing the many-to-many association between the food
     and the category table  """

    def __init__(self):
        """Attributes represent the data from the food_store table:
        food_id and category_id """

        self.category_id = None
        self.food_id = None
