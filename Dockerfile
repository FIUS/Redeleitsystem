FROM python:3
ADD . /app

RUN pip install -r /app/requirements.txt
RUN python3 /app/dump.py

EXPOSE 5000

CMD ["python3","/app/server.py","runserver","--host","0.0.0.0"]
