from .base import Node

class DataNode(Node):

    def set_data(self, data):
        self.data.on_next(data)
