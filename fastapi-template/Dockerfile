FROM --platform=amd64 ubuntu:22.04
WORKDIR /code/
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install python3-dev python3-pip build-essential gcc curl netcat logrotate -y
COPY fastapi-template/requirements.txt /code/requirements.txt
COPY fastapi-template/application /code/
COPY fastapi-template/certificates /code/certificates
COPY fastapi-template/entrypoint.sh /code/entrypoint.sh
RUN chmod +x entrypoint.sh
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
CMD /code/entrypoint.sh