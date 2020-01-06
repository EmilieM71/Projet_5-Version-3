class FoodStore:
    """ This class representing the many-to-many association between the food
     and store table """

    def __init__(self):
        """ Attributes represent the data from the food_store table:
        food_id and store_id. """

        self.food_id = None
        self.store_id = None
