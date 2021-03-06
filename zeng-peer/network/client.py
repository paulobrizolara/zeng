import socket
import pickle

from .server import send_data

def create_client_socket(target_host, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    return client


def receive_data(socket):
    f = socket.makefile('rb', 1024)
    data = pickle.load(f)
    f.close()
    return data

def do_request(socket, type, **data_members):
    request = {}
    request['task'] = type

    for k in data_members:
        request[k] = data_members[k]

    #send request
    send_data(socket, request)

    #receive response
    return receive_data(socket) #TODO: implement timeout
