import socket
import time
import json
import threading

#create the sub resolvers socket
resolver_client_socket = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

server_addr = ('127.0.0.10', 53053)
resolver_client_socket.bind(server_addr)

#initialize a payload with the desired keys
payload_dict ={
    "dns.flags.response": "placeholder",
    "dns.flags.recdesired": "placeholder",
    "dns.qry.name": "placeholder",
    "dns.qry.type": "placeholder",
    "dns.flags.rcode": "placeholder",
    "dns.count.answers": "placeholder",
    "dns.flags.authoritative": "placeholder",
    "dns.a": "placeholder",
    "dns.ns": "placeholder",
    "dns.resp.ttl": 1234,
    "dns.srv.name": "placeholder",
    "dns.srv.port": "placeholder",
    "dns.srv.proto": "placeholder",
    "dns.srv.service": "placeholder",
    "dns.srv.target": "placeholder"
}

#convert dict to json object
payload_json = json.dumps(payload_dict, indent = 4)

#This class is just to start a thread and wait for packages
class Recursive_resolver(object):
    def __init__(self, seconds=2000):
        self.seconds = seconds

    def start(self):
        print('Resolver start listening for ', self.seconds, ' seconds...')
        start = time.time()
        time.perf_counter()
        elapsed = 0
        while elapsed < self.seconds:
            elapsed = time.time() - start
            # time.sleep(100)
            payload, client_addr = resolver_client_socket.recvfrom(1024)
            payload = json.loads(payload)
            print('Received response from: ', client_addr, ' with payload:\n', json.dumps(payload, indent=4))

        print('Resolver stopped listening after ', elapsed, ' seconds.')

print(bla)

resolver = Recursive_resolver(seconds=60)
resolver_thread = threading.Thread(target=resolver.start)
resolver_thread.start()

#send a request to a dns server
resolver_client_socket.sendto(bytes(payload_json, 'utf-8'),('127.0.0.15',53053))