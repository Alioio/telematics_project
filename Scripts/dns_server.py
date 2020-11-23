import socket
import time
import json

#create this servers UDP socket
server_socket = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

#bind the socket to a ip and port
server_addr = ('127.0.0.15', 53053)
server_socket.bind(server_addr)

def respond_to_client(payload, client_addr):
    try:
        payload['dns.flags.response'] = 'Changed!'
        payload_json = json.dumps(payload, indent = 4)
        #time.sleep(100)
        server_socket.sendto(bytes(payload_json, 'utf-8'), client_addr)
    except:
        print('could not respond to client: ',client_addr)

#Wait for requests from clients (resolver)
while(True):
    payload, client_addr = server_socket.recvfrom(1024)
    payload = json.loads(payload)
    print('received a request from client: ',client_addr,'with payload:\n',json.dumps(payload, indent = 4))
    respond_to_client(payload, client_addr)