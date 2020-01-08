from controller.manage_controller import ManageController


class Controller:

    def __init__(self):
        self.controller = ManageController()

    def starting(self):
        """ This method is responsible for display start view"""
        self.go_to_controller_start()

    def go_to_controller_start(self):
        self.controller.cont_start.shows_start_view()

    # def display_steps_view(self):
    #     self.controller.cont_steps.shows_steps_view()
