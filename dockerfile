FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT 3548
EXPOSE 3548

COPY ./app /app