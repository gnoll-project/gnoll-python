import dispatch from .dispatch

def update_node(node_id, properties):
    dispatch.emit('action', {
        'type': 'UPDATE_NODE',
        'id': node_id,
        'properties': properties
    })
