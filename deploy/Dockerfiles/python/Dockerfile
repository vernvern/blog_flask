# python
FROM python:3.6.4-jessie as python
WORKDIR /opt/src

COPY ./requirements.txt /opt/src/
COPY ./sources.list /opt/src/

RUN mv ./sources.list /etc/apt/sources.list \
    && apt-get -y update \
    && apt-get install -y python3-pip python3-dev \
    && pip3 install -r /opt/src/requirements.txt --no-cache-dir \
    && rm -rf /opt/src/requirements.txt \
    && apt-get  -y autoremove \
    && apt-get -y autoclean

VOLUME ['/opt/script', '/opt/log', '/opt/data', '/opt/src']

CMD python3 manage.py runserver

