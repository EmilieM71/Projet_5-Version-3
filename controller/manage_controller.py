from view.manage_view import ManageView
from controller.controller_start import ControllerStart
from controller.controller_steps import ControllerSteps
from controller.controller_user import ControllerUser
from controller.controller_cat import ControllerCat


class ManageController:
    """ This class allows you to:
        - create an object for each controller in the program
        - switch from one controller to another
        - be the link with the view management class"""

    def __init__(self):
        self.view = ManageView()
        self.cnx = None
        self.info_user = None
        self._cont_start = ControllerStart(self)
        self._cont_steps = None
        self._cont_user = None
        self._cont_cat = None

    def starting(self):
        self.view.create_root()
        self.view.parameter_root()
        self._cont_start.shows_start_view()

    # ___Methods and property of the 'cont_start_up' attribute___ #
    def _get_cont_start(self):
        """ The method called to access the 'cont_start' attribute."""
        return self._cont_start

    # Property of the cont_start attribute
    cont_start = property(_get_cont_start)

    # ___Methods and property of the 'cont_steps' attribute___ #
    def _get_cont_steps(self):
        """ The method called to access the 'cont_steps' attribute. If it has
        no value, an instance of the ControllerSteps class is created, and then
        it is assigned that object """
        if self._cont_steps is None:
            import_class = ControllerSteps(self)
            self._set_cont_steps(import_class)
        return self._cont_steps

    def _set_cont_steps(self, new_value):
        """ Method called to change the value of the 'cont_steps' attribute """
        self._cont_steps = new_value

    # Property of the cont_brand attribute
    cont_steps = property(_get_cont_steps, _set_cont_steps)

    # ___Methods and property of the 'cont_user' attribute___ #
    def _get_cont_user(self):
        """ The method called to access the 'cont_user' attribute. If it has
        no value, an instance of the ControllerUser class is created, and then
        it is assigned that object """
        if self._cont_user is None:
            import_class = ControllerUser(self)
            self._set_cont_user(import_class)
        return self._cont_user

    def _set_cont_user(self, new_value):
        """ Method called to change the value of the 'cont_user' attribute """
        self._cont_user = new_value

    # Property of the cont_user attribute
    cont_user = property(_get_cont_user, _set_cont_user)

    # ___Methods and property of the 'cont_cat' attribute___ #
    def _get_cont_cat(self):
        """ The method called to access the 'cont_cat' attribute. If it has
        no value, an instance of the ControllerCat class is created, and then
        it is assigned that object """
        if self._cont_cat is None:
            import_class = ControllerCat(self, )
            self._set_cont_cat(import_class)
        return self._cont_cat

    def _set_cont_cat(self, new_value):
        """ Method called to change the value of the 'cont_cat' attribute """
        self._cont_cat = new_value

    # Property of the cont_cat attribute
    cont_cat = property(_get_cont_cat, _set_cont_cat)