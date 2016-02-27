import socket
import json
from random import random

from .actions.dispatch import dispatch
from .nodes.base import Node
from .selection import Selection


class GnollClient(object):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 7999
    # BUFFER_SIZE = 1024

    def __init__(self):
        self.open_socket()
        dispatch.on('action', self.send_message)

    def open_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.TCP_IP, self.TCP_PORT))

    def shutdown(self):
        self.socket.close()

    def send_message(self, msg):
        msg = json.dumps(msg)
        self.socket.send(msg)

    def parse_spec(self, spec):
        nodes = spec['nodes']
        edges = spec['edges']

        node_map = {}
        for node in nodes:
            node_map[int(node['id'])] = Node.create(node)

        for key, value in edges.iteritems():
            in_node = node_map[int(key)]
            out_node = node_map[int(value)]

            in_node.send_to(out_node)

        return Selection(node_map.values())
