

class Selection(object):
    def __init__(self, nodes):
        self.nodes = nodes

    def find_by_id(self, id):
        # return the first match
        return next((node for node in self.nodes if node.attrs['id'] == id), None)
