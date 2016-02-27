from .base import Node

class TransformNode(Node):

    def set_transform(self, transform):
        self.transform = transform

    def on_data(data):
        self.data.on_next(self.transform(data))
