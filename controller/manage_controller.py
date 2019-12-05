from view.manage_view import ManageView
from controller.controller_start import ControllerStart


class ManageController:
    """ This class allows you to:
        - create an object for each controller in the program
        - switch from one controller to another
        - be the link with the view management class"""

    def __init__(self):
        self.view = ManageView()
        self._cont_start = ControllerStart(self)

    def starting(self):
        self.view.create_root()
        self.view.parameter_root()
        self._cont_start.shows_start_view()

    def create_new_class_instance(self, import_class):
        """ This method creates a new class instance and assigns this object
        to the local variable. """
        class_object = import_class(root=self.view.root)
        # cnx=self.cnx,
        # info_user=self.info_user,
        # info_cat=self.info_cat,
        # list_id_food=self.list_id_food
        return class_object

    # ___Methods and property of the 'cont_start_up' attribute___ #
    def _get_cont_start(self):
        """ The method called to access the 'cont_start' attribute."""
        return self._cont_start

    # Property of the cont_start attribute
    cont_start = property(_get_cont_start)
