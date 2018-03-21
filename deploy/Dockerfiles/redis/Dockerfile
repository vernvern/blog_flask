# redis
FROM redis:4.0.8
WORKDIR /opt/src
EXPOSE 6379
VOLUME ['/opt/script', '/opt/log', '/opt/data', '/opt/src']
CMD redis-server --appendonly yes
