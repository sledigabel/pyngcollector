FROM alpine:latest
MAINTAINER sledigabel@gmail.com

RUN apk update
RUN apk add gcc python python-dev py-pip libpcap libpcap-dev libdnet g++

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY test.py /tmp
RUN chmod 755 /tmp/test.py

CMD /bin/sh
