FROM nginx:1.13.9
COPY ./nginx.conf /etc/nginx/nginx.conf
VOLUME ['/opt/log']
RUN mkdir /opt/log/nginx -p  \
    && touch /opt/log/nginx/error.log \
    && touch /opt/log/nginx/access.log \
    && chown -R nginx /opt
# CMD ["nginx", "-g", "daemon off;", "-c", "/opt/src/blog/deploy/Dockerfiles/nginx/nginx.conf"]
CMD /bin/sh -c "while true; do echo hello world; sleep 1; done"
