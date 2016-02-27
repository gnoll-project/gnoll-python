from .base import Node
from gnoll.actions.nodes import update_node

class SinkNode(Node):

    def on_data(self, data):
        update_node(self.attrs['id'], {
            'data': data
        })
