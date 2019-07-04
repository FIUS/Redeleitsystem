# source environment
FROM scratch AS source

COPY .docker/ /.docker/
COPY requirements.txt /app/
COPY src /app/src

FROM python:3
COPY --from=source /app/ /app/
COPY --from=source .docker/dockerize-templates/* /etc/dockerize-templates/

RUN pip install -r /app/requirements.txt

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENV DB_URI sqlite:///db.db
ENV SECRET_KEY secret
ENV ADMIN_USER admin
ENV ADMIN_PASS pass

EXPOSE 5000
CMD ["dockerize", "-template", "/etc/dockerize-templates/config.py.tmpl:/app/src/config.py", "python3","/app/src/server.py","runserver","--host","0.0.0.0"]
