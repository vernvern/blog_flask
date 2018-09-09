FROM nginx:1.13.9
COPY ./nginx.conf /etc/nginx/nginx.conf
VOLUME ['/opt/log']
RUN chown -R nginx /opt
CMD ["nginx", "-g", "daemon off;", "-c", "/opt/src/blog/deploy/Dockerfiles/nginx/nginx.conf"]
