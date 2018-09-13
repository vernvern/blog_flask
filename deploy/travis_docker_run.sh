(docker inspect blog_python) > /dev/null 2>&1
if [ "$?"v = "0"v ] ; then
    echo 'docker rm blog_python:'
    docker rm -f blog_python
fi

docker run --name blog_python -d -v /home/travis/build/vernvern/blog_flask/log:/opt/log -v  /home/travis/build/vernvern/blog_flask:/opt/src/blog blog:python-3.6.4
