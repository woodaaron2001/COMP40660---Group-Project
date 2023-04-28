
#!/usr/bin/env python3
# ipc_client.py
import os
import socket
import random
import json
import time
import datetime 
import numpy as np

HOST = socket.gethostbyname('ipc_server_dns_name')    # The server's hostname or IP address
PORT = 9898         # The port used by the server
imageDir = './images'
counter = 0

totalTimeToSend = []
computationTime = []

#Connect to the server via socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    #loop through all files in the image directory
    for filename in os.listdir(imageDir):
        startTime = time.time()
        f = os.path.join(imageDir,filename)

        if not os.path.isfile(f):
            continue
        counter +=1
        print("---IMAGE ",counter,"---")

        #First we want to send the byte count of the file to our server
        imageFile = open(f,'rb')
        bytes = imageFile.read()
        size = len(bytes)
        
        #SIZEDATA, is used so we can parse what type of message we got in server
        size = "SIZEDATA," + str(size)
        s.sendall(str(size).encode())

        #Receive ack
        ack = s.recv(4096)
        ack = str(ack.decode())
        
        if ack != "ACK":
            print("Error sending image")
            print("Received: ",ack)
            exit(0)
        print('Received', repr(ack))
        s.sendall(bytes)

        # check what server send
        answer = s.recv(8096)
        answer = (answer.decode())
        print('Received Data',str(answer))
        computationTime.append(float(answer.partition("ProcessTime: ")[2]))
        elapsed_time = time.time() - startTime
        totalTimeToSend.append(elapsed_time)
        print("Total Time: ",elapsed_time)

print("------PARAMETRIC RESULTS------")
meanTTS = np.mean(totalTimeToSend)
meanComputation = np.mean(computationTime)
stdTTs = np.std(totalTimeToSend)

print("MEAN Total Time: ", meanTTS)
print("Mean Computation Time: ", meanComputation)
print("Co Variation of TotalTime: ",stdTTs/meanTTS)

