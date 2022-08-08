FROM ubuntu:latest
RUN apt-get update
RUN apt-get install python3 -y
WORKDIR /usr/app/src
COPY python.py ./
CMD ["python3", "./python.py"]
