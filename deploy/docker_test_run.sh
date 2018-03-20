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

# rm network
(docker network inspect net) > /dev/null 2>&1
if [ "$?"v != "0"v ] ; then
    echo 'docker network rm net:'
    docker network create --subnet=172.18.0.0/16  net
fi

# rebuild
if [ "$CI"v = "true"v ]; then
    mkdir /home/travis/build/vernvern/log
    docker run --name blog_python -d -v /Volumes/log:/opt/log -v /home/travis/build/vernvern/blog:/opt/src -p 8000:8000 --network net --ip 172.18.0.3 blog:python-3.6.4
    docker run --name blog_redis -p 6379:6379 -d  --network net --ip 172.18.0.2 blog:redis-4.0.8
else
    docker run --name blog_redis -p 6379:6379 -d  --network net --ip 172.18.0.2 blog:redis-4.0.8
    docker run --name blog_python -d -v /Volumes/log:/opt/log -v /Users/vernli/python/blog:/opt/src -p 8000:8000 --network net --ip 172.18.0.3 blog:python-3.6.4
    docker run --name blog_nginx -p 80:80 -d -v /Volumes/log:/opt/log --network net --ip 172.18.0.4 blog:nginx-1.13.9
fi
