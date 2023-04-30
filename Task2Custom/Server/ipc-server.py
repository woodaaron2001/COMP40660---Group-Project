
#!/usr/bin/env python3
# ipc_server.py

import socket
from imageai.Detection import ObjectDetection
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import io
import time
import datetime


detector = ObjectDetection()

#pip install, imageai, pytorch, torchvision, opencv-python,tensorflow, keras


# defining the paths  
path_model = "./Models/tiny-yolov3.pt"  
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(path_model) 
detector.loadModel()


counter = 0
HOST = socket.gethostbyname('offloadingserver')  # Standard loopback interface address (localhost)
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)
myRecvSize = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
    
        with conn:
            
            counter+=1
            
            while True:
                
                data = conn.recv(myRecvSize)
                if not data:
                    break
                txtData = str(data)

                #Setting buffersize on receiving data
                if(txtData.startswith("b\'SIZEDATA")):
                    myRecvSize = 409600000
                    txtData = str(data.decode())
                    x = txtData.split(',')
                    myRecvSize = int(x[1])

                    conn.sendall("ACK".encode())


                else:
                    #Timing computation time
                    startProcessTime = time.time()
                    
                    myRecvSize = 409600000
                    # Convert the received bytes data to a Pillow Image object
                    image = Image.open(io.BytesIO(data))
                    image = image.convert('RGB')
                    
                    # Pass the input image to the object detection model
                    detections = detector.detectObjectsFromImage(input_image=image)
                    
                    result = ""
                    
                    # Process the output of the model
                    for detection in detections:
                        result += detection["name"] +  " : " +  str(detection["percentage_probability"]) + " : " +  str(detection["box_points"]) + "\n"
                    
                    #Formatting results
                    elapsed_time = time.time() - startProcessTime
                    result += "ProcessTime: "+str(elapsed_time)
                    conn.sendall(result.encode())
                    break

