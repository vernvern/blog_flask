# stop python docker
(docker inspect blog_python) > /dev/null 2>&1
if [ $? == '0' ] ; then
    echo 'docker stop blog_python:'
    docker stop blog_python
    echo 'docker rm blog_python:'
    docker rm blog_python
fi

# stop redis docker
(docker inspect blog_redis) > /dev/null 2>&1
if [ $? == '0' ] ; then
    echo 'docker stop blog_redis:'
    docker stop blog_redis
    echo 'docker rm blog_redis:'
    docker rm blog_redis
fi

# rm network
(docker network inspect net) > /dev/null 2>&1
if [ $? == '0' ] ; then
    echo 'docker network rm net:'
    docker network rm net
fi

# rebuild
docker network create --subnet=172.18.0.0/16  net
docker run --name blog_python -d -v /Volumes/log:/opt/log -v /Users/vernli/python/blog:/opt/src -p 5000:5000 --network net --ip 172.18.0.3 blog:python-3.6.4
docker run --name blog_redis -p 6379:6379 -d  --network net --ip 172.18.0.2 blog:redis-4.0.8
