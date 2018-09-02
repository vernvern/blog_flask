# python 基础镜像
FROM python:3.6.4-jessie as base
WORKDIR /opt/src

FROM python:3.6.4-jessie as release
WORKDIR /opt/src
EXPOSE 8000
COPY /opt/src/blog/deploy/Dockerfiles/python/requirements.txt /opt/src/
RUN pip install --upgrade pip \
    && pip install -r /opt/src/requirements.txt --no-cache-dir
VOLUME ['/opt/script', '/opt/log', '/opt/data', '/opt/src']
CMD gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
