# Get the latest base image for python
FROM python:latest
# Put files at the image '/server/' folder.
ADD ipc-server.py /server/
# '/server/' is base directory
WORKDIR /server/
# Expose port 9898 in the container
EXPOSE 9898
# execute the command
CMD [ "python3", "/server/ipc-server.py" ]