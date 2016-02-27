from .base import Node
from gnoll_python.actions.nodes import update_node

class SinkNode(Node):
    def on_data(data):
        update_node(self.attrs[id], {
            'data': data
        })
