(docker inspect blog_python) > /dev/null 2>&1
if [ "$?"v = "0"v ] ; then
    echo 'docker rm blog_python:'
    docker rm -f blog_python
fi

docker run --name blog_python -d -v /home/travis/build/vernvern/blog/log:/opt/log -v  /home/travis/build/vernvern/blog:/opt/src blog:python-3.6.4
