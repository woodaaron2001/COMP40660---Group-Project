# Get the latest base image for python
FROM python:latest
RUN pip install --no-cache-dir --upgrade pip
RUN pip install opencv-python
RUN pip install tensorflow
RUN pip install keras
RUN pip install torchvision
RUN pip install pytorch
RUN pip install imageai
ADD ./Models/tiny-yolov3.pt /server/Models
# Put files at the image '/server/' folder.
ADD ipc-server.py /server/
# '/server/' is base directory
WORKDIR /server/
# Expose port 9898 in the container
EXPOSE 9898
# execute the command
CMD [ "python3", "/server/ipc-server.py" ]