from gnoll import GnollClient
import json
from random import random

transform_spec = json.loads('{"nodes":[{"id":0,"width":300,"height":300,"component":"DATA_COMPONENT","nodeType":"DATA_NODE","position":{"x":107.453125,"y":141}},{"id":1,"width":300,"height":300,"component":"SLIDER_COMPONENT","nodeType":"TRANSFORM_NODE","position":{"x":143.453125,"y":242}},{"id":2,"width":300,"height":300,"component":"SCATTER_COMPONENT","nodeType":"SINK_NODE","position":{"x":119.453125,"y":431}}],"edges":{"0":1,"1":2}}')


gnoll = GnollClient()
nodes = gnoll.parse_spec(transform_spec)

data_node = nodes.find_by_id(0)
transform_node = nodes.find_by_id(1)

def t(data, transform_attrs):
    l = len(data)
    x = transform_attrs.get('x', 100.0)
    idx = int(x / 100.0 * l)
    return data[:idx]

transform_node.set_transform(t)


setdata = []
for i in range(200):
    setdata.append({
        'x': random() * 10,
        'y': random() * 10
    })

data_node.set_data(setdata)
