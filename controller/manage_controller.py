from controller.controller_start import ControllerStart
from controller.controller_steps import ControllerSteps
from controller.controller_user import ControllerUser
from controller.controller_welcome import ControllerWelcome
from controller.controller_cat import ControllerCat
from controller.controller_food import ControllerFood
from model.manage_db.cnx_db import CnxDatabase


class ManageController:
    """ This class allows to pass from a controller to another in the
    application"""

    def __init__(self):
        self.cont_start = ControllerStart(self)
        self._cnx = None
        self._cont_steps = None
        self._cont_user = None
        self._info_user = None
        self._cont_welcome = None
        self._cont_cat = None
        self._selected_category = None
        self._cont_food = None

    def _get_cnx(self):
        if self._cnx is None:
            cnx_db = CnxDatabase()
            self._cnx = cnx_db.connection()
        return self._cnx

    cnx = property(_get_cnx)

    def _get_cont_steps(self):
        if self._cont_steps is None:
            self._cont_steps = ControllerSteps(self)
        return self._cont_steps

    cont_steps = property(_get_cont_steps)

    def _get_cont_user(self):
        if self._cont_user is None:
            self._cont_user = ControllerUser(self)
        return self._cont_user

    cont_user = property(_get_cont_user)

    def _get_info_user(self):
        if self._info_user is None:
            self._info_user = self._cont_user.info_user
        return self._info_user

    def _set_info_user(self, new_info_user):
        self._info_user = new_info_user

    info_user = property(_get_info_user, _set_info_user)

    def _get_cont_welcome(self):
        if self._cont_welcome is None:
            self._cont_welcome = ControllerWelcome(self)
        return self._cont_welcome

    cont_welcome = property(_get_cont_welcome)

    def _get_cont_cat(self):
        if self._cont_cat is None:
            self._cont_cat = ControllerCat(self)
        return self._cont_cat

    cont_cat = property(_get_cont_cat)

    def _set_selected_cat(self, new_cat):
        self._selected_category = new_cat

    def _get_selected_cat(self):
        return self._selected_category

    selected_category = property(_get_selected_cat, _set_selected_cat)

    def _get_cont_food(self):
        if self._cont_food is None:
            self._cont_food = ControllerFood(self)
        return self._cont_food

    cont_food = property(_get_cont_food)
