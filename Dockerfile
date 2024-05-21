FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt --break-system-packages

EXPOSE 3000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]


