FROM ubuntu:20.04
COPY . /home/nilut
RUN apt-get update -y
RUN apt-get upgrade -y
WORKDIR /home/nilut
RUN apt install python3-pip -y
RUN pip3 install requirements.txt
CMD python3 -h app.py
