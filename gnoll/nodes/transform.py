from .base import Node

class TransformNode(Node):

    def __init__(self, node_dict):
        super(self.__class__, self).__init__(node_dict)
        self._data = None

    def compute_output(self, data):
        return self.transform(data, self.attrs.get('transformAttributes', {}))

    def set_attrs(self, attrs):
        self.attrs.update(attrs)
        print 'setting attrs'
        if self._data is not None:
            print 'sending next data'
            self.data.on_next(self.compute_output(self._data))

    def set_transform(self, transform):
        self.transform = transform
        if self._data is not None:
            self.data.on_next(self.compute_output(self._data))

    def on_data(self, data):
        self._data = data
        self.data.on_next(self.compute_output(data))
