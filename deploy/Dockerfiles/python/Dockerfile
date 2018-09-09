# python 基础镜像

FROM python:3.6.4-jessie
WORKDIR /opt/src/blog
EXPOSE 8000
COPY ./requirements.txt /opt/src/blo
RUN pip install --upgrade pip \
    &&  pip install -r /opt/src/requirements.txt --no-cache-dir
VOLUME ['/opt/script', '/opt/log', '/opt/data', '/opt/src']
CMD gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
