# command

## build
`in blog root`
docker build --target debug -t blog:python-3.6.4 ./deploy/Dockerfiles/python
docker build -t blog:redis-4.0.8 ./deploy/Dockerfiles/redis
docker build -t blog:nginx-1.13.9 ./deploy/Dockerfiles/nginx
