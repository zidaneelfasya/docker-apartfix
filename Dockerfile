FROM ubuntu:latest


RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt --break-system-packages


EXPOSE 3000


CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
