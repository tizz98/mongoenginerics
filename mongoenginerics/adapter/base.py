from mongoengine import connect

class MongoEnginericsAdapter():
    _controllers = []

    def __init__(self, database=''):
        self._connection = connect(database)

    def add_controller(self, ctrl):
        self._controllers.append(ctrl)

    def get_app(self):
        raise Exception('@todo')

    def attach(self):
        raise Exception('@todo')
