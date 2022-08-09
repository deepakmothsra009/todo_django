FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY todo_task.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/todo_task.conf /etc/nginx/sites-enabled/ \
    && rm /etc/nginx/conf.d/default.conf
