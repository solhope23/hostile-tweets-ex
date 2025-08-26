

class FastApiEndpoint:

    def __init__(self, app, app_manager):
        self.app_manager = app_manager
        self.app = app
        self.all_endpoint()

    def all_endpoint(self):
