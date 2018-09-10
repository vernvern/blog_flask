FROM nginx:1.13.9
COPY ./nginx.conf /etc/nginx/nginx.conf
RUN chown -R nginx /opt
# CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
CMD /bin/sh -c "while true; do echo hello world; sleep 1; done"
