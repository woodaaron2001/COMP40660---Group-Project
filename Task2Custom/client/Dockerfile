FROM woodaaron2001/offloadingclient:latest

RUN rm /client/images/*

ADD /images /client/images

ADD ipc-client.py /client/
# '/server/' is base directory
WORKDIR /client/
# execute the command
CMD sleep 6 && python3 /client/ipc-client.py