FROM python:3.8.0-slim

WORKDIR /python-support

RUN apt-get update && apt-get install -y curl
COPY ./requirements.txt /python-support/requirements.txt
RUN pip install -r /python-support/requirements.txt
COPY ./scripts /python-support/scripts
COPY ./protobuf /python-support/protobuf
COPY ./cloudstate /python-support/cloudstate
COPY ./example /python-support/example
COPY ./shoppingcart /python-support/shoppingcart
COPY ./functiondemo /python-support/functiondemo
COPY ./setup.py /python-support/setup.py
COPY ./Description.md /python-support/Description.md


RUN pip install . -vvv

WORKDIR ~
ENTRYPOINT ["python", "-m", "example.tck_services"]

EXPOSE 8080