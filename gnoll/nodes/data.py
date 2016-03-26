from .base import Node

class DataNode(Node):

    def set_data(self, data):
        self.data.on_next(data)

    def compute_output(self):
        return self.transform()

    def set_transform(self, transform):
        self.transform = transform
        self.data.on_next(self.compute_output())
