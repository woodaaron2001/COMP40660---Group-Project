FROM woodaaron2001/offloadingserver:latest
# '/server/' is base directory
ADD ipc-server.py /server/
WORKDIR /server/
# Expose port 9898 in the container
EXPOSE 9898
# execute the command
CMD [ "python3", "/server/ipc-server.py" ]