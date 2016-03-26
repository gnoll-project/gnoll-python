import SocketServer
import socket
import json
from random import random
import threading

from .actions.dispatch import dispatch
from .nodes.base import Node
from .selection import Selection
import signal
from time import sleep

TCP_IP = '127.0.0.1'
TCP_PORT_SERVER = 7998
TCP_PORT_CLIENT = 7999
BUFFER_SIZE = 1024

class TCPHandler(SocketServer.BaseRequestHandler):

    def __init__(self, callback, *args, **keys):
        self.callback = callback
        SocketServer.BaseRequestHandler.__init__(self, *args, **keys)

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(BUFFER_SIZE).strip()
        self.callback(json.loads(data))


def TCPHandlerFactory(callback):
    def createHandler(*args, **keys):
        return TCPHandler(callback, *args, **keys)
    return createHandler

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class GnollClient(object):

    def __init__(self):
        self.selection = Selection([])
        self.open_socket()
        dispatch.on('action', self.send_message)

    def handle_incoming_data(self, data):
        node = self.selection.find_by_id(data['id'])
        node.set_attrs(data['properties'])

    def open_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((TCP_IP, TCP_PORT_CLIENT))
        self.server = ThreadedTCPServer((TCP_IP, TCP_PORT_SERVER), TCPHandlerFactory(self.handle_incoming_data))
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        self.server_thread.daemon = True
        self.server_thread.start()

    # def run(self):
    #     while True:
    #         sleep(1)

    def shutdown(self):
        self.socket.close()
        self.server_thread.join()
        self.server.shutdown()
        self.server.server_close()

    def send_message(self, msg):
        msg = json.dumps(msg)
        self.socket.send(msg)

    def parse_spec(self, spec):
        nodes = spec['nodes']
        edges = spec['edges']

        node_map = {}
        for node in nodes:
            existing_node = self.selection.find_by_id(node['id'])
            if existing_node is None:
                node_map[int(node['id'])] = Node.create(node)
            else:
                node_map[int(node['id'])] = existing_node

        for key, value in edges.iteritems():
            in_node = node_map[int(key)]
            out_node = node_map[int(value)]

            in_node.send_to(out_node)

        self.selection = Selection(node_map.values())
        return self.selection
