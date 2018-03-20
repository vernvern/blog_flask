# python 基础镜像
FROM python:3.6.4-jessie as base
WORKDIR /opt/src

# 依赖
FROM base as dependencies
COPY ./requirements.txt /opt/src/
RUN pip install --upgrade pip \
    && pip install -r /opt/src/requirements.txt --no-cache-dir

# 复制项目文件, build
FROM dependencies as debug
WORKDIR /opt/src
VOLUME ['/opt/script', '/opt/log', '/opt/data', '/opt/src']
CMD gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app

# 发布
FROM python:3.6-alpine3.7 as release
WORKDIR /opt/src
COPY ./requirements.txt /opt/src/
RUN pip install --upgrade pip \
    && pip install -r /opt/src/requirements.txt --no-cache-dir
VOLUME ['/opt/script', '/opt/log', '/opt/data', '/opt/src']
CMD gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app
