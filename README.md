# COMP40660 Autonomous Vehicle Offloading

## Requirements
 - Docker (version 20.10.0 or higher)
 
## Setup
  1. Clone This repository
  2. CD to "task2CustomOffloading"
  3. Build the docker images using "docker-compose build"
  (If needed the non custom offloading implementation is run directly in the cli as outlined in the report)
  
## Synopsis 
The main ideas are detailed in the report however here are the main details:

Design: Train model, send it to the edge, compute heavy lifting of image recognition
![design](https://github.com/woodaaron2001/COMP40660---Group-Project/blob/main/READMEIMAGES/IDEA.png)

Implementation: Cars send images to the server which in turn return the bounding boxes and names of objects located in the image
![Edge](https://github.com/woodaaron2001/COMP40660---Group-Project/blob/main/READMEIMAGES/EDGE.png)

## Code:

Client sends an initiation telling the server how large the image will be.
Server updates the buffer and sends an ACK.
Client receives this and sends the image
Server processes the images and sends the location of objects
![code](https://github.com/woodaaron2001/COMP40660---Group-Project/blob/main/READMEIMAGES/CODE.png)

## EXTRA DOCKER LINKS FOR THE ASSIGNMENT




  
 


 
