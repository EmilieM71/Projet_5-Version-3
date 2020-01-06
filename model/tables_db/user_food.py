class UserFood:
    """ This class representing the many-to-many association between the food
     and the category table  """

    def __init__(self):
        """Attributes represent the data from the user_food table """
        self.user_id = None
        self.food_id = None
        self.substitute_id = None