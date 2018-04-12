FROM tiangolo/uwsgi-nginx-flask:python3.6

# RUN mkdir app
# WORKDIR /app

# COPY ./app/requirements.txt /app
# RUN pip3 install --no-cache-dir -r requirements.txt

# ENV LISTEN_PORT 3548
# EXPOSE 3548

COPY ./app /app
RUN pip3 install --no-cache-dir -r requirements.txt

