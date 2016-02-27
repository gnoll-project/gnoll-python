class Node(object):
    def __init__(self, node_dict):
        self.data = Subject()
        self.attrs = node_dict


    def send_to(self, to_node):
        self.data.subscribe(to_node.on_data)


    @staticmethod
    def create(node_dict):
        from .data import DataNode
        from .transform import TransformNode
        from .sink import SinkNode
        from rx.subjects import Subject

        node_type_map = {
            'DATA_NODE': DataNode,
            'TRANSFORM_NODE': TransformNode,
            'SINK_NODE': SinkNode
        }

        node_type = node_dict['nodeType']
        return node_type_map[node_type](node_dict)
