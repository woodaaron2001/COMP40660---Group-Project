
#!/usr/bin/env python3
# ipc_client.py

import socket
import random
import json

HOST = socket.gethostbyname('ipc_server_dns_name')    # The server's hostname or IP address
PORT = 9898        # The port used by the server

sendParameters = []

#generating 500 parametric values
for i in range(100):
    #generate random value between 0 and 10 
    sendParameters.append(random.randint(0,1000))

sendData = data = json.dumps(sendParameters)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(sendData.encode()) 
    data = s.recv(1024)

print('Received', repr(data))