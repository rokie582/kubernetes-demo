FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip
RUN pip3 install flask

COPY sample-flask.py /opt/sample-flask.py

ENTRYPOINT FLASK_APP=/opt/sample-flask.py flask run --host=0.0.0.0