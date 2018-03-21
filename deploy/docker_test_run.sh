#! /bin/bash

# stop python docker
(docker inspect blog_python) > /dev/null 2>&1
if [ "$?"v = "0"v ] ; then
    echo 'docker rm blog_python:'
    docker rm -f blog_python
fi

# stop redis docker
(docker inspect blog_redis) > /dev/null 2>&1
if [ "$?"v = "0"v ] ; then
    echo 'docker rm blog_redis:'
    docker rm -f blog_redis
fi

# stop nginx docker
(docker inspect blog_nginx) > /dev/null 2>&1
if [ "$?"v = "0"v ] ; then
    echo 'docker rm blog_nginx:'
    docker rm -f blog_nginx
fi

(docker network inspect net) > /dev/null 2>&1
if [ "$?"v != "0"v ] ; then
    docker network create --subnet=192.168.1.1/24  net
fi

# rebuild
if [ "$CI"v = "true"v ]; then
    mkdir /home/travis/build/vernvern/log
    docker run --name blog_python -d -v /opt/log:/opt/log -v /root/blog:/opt/src -p 8000:8000 --network net --ip 192.168.1.3 blog:python-3.6.4
    docker run --name blog_redis -p 6379:6379 -d  --network net --ip 192.168.1.2 blog:redis-4.0.8
else
    docker run --name blog_redis -p 6379:6379 -d  --network net --ip 192.168.1.2 blog:redis-4.0.8
    docker run --name blog_python -d -v /opt/log:/opt/log -v /root/blog:/opt/src --network net --ip 192.168.1.3 blog:python-3.6.4
    docker run --name blog_nginx -p 80:80 -d -v /opt/log:/opt/log -v /root/blog:/opt/src --network net --ip 192.168.1.4 blog:nginx-1.13.9
fi
