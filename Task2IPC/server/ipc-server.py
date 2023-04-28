#!/usr/bin/env python3
# ipc_server.py

import socket
import ast
from collections import defaultdict

HOST = socket.gethostbyname('ipc_server_dns_name')  # Standard loopback interface address (localhost)
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                #receive the parameters as a list of strings b['1','2'] etc and decode
                params = data.decode()
                paramList = ast.literal_eval(params)

                #Mean is sum/length
                mean = sum(paramList) / len(paramList)

                #Find occurence of each and store in an occDict, get the max of that dict
                occDict = defaultdict(int)
                for param in paramList:
                    occDict[param] +=1
                mode = max(occDict, key=occDict.get)

                median = 0
                paramList.sort()
                paramLength = len(paramList)
                if paramLength % 2 == 0:
                    left = paramList[paramLength//2-1] 
                    right = paramList[paramLength//2]
                    median = (left+right)/2
                else:
                    median = paramList[paramLength//2]
                    


                results = "Mean: " + str(mean) + " Median: " + str(median) + " Mode: " + str(mode)
                print("Received: ",len(params),"Parameters")
                print(results)
                
                # Send the mean back to the client as a string
                conn.sendall(results.encode())