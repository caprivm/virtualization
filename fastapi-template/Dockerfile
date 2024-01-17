FROM --platform=linux/amd64 ubuntu:22.04
WORKDIR /code/
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install python3-dev python3-pip build-essential curl gcc libpq-dev logrotate netcat -y
COPY requirements.txt /code/requirements.txt
COPY application /code/
COPY certificates /code/certificates
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x entrypoint.sh
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
CMD /code/entrypoint.sh