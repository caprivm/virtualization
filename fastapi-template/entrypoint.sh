#!/bin/bash
usage="usage: ./$(basename "$BASH_SOURCE")  [-h] [-s]

Script to initialize the API using FastAPI, celery and flower in the same container.
The API can run on HTTP or HTTPS based on your requirements. Below the flags that could
be used in the script. 

Optional arguments:
    -h, --help      Show help message and exit.
    -s, --ssl       Flag to run the application on HTTPS. The certificates must to be on the certificates folder.

Example of use:
./$(basename "$BASH_SOURCE") -s
"

# Default variables
SSL_ENABLED=false
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Get options
TEMP=$(getopt \
  --options "hs" \
  --longoptions help,ssl \
  --name "$(basename "$BASH_SOURCE")" \
  -- "$@"
)
eval set -- "$TEMP"
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h | --help)
    echo "$usage"; exit 0; shift 2
    ;;
    -s | --ssl)
    SSL_ENABLED=true; shift 2
    ;;
    --)
    shift; break
    ;;
    *)
    break
    ;;
  esac
done

cd $DIR
echo "DEBUG: SSL_ENABLED: $SSL_ENABLED"

# Celery Execution
rm -rf /var/run/celery/*
# celery -A config.config_celery worker --pool=gevent --concurrency=500 --loglevel=INFO --logfile=/code/logs/celery.log -O fair -Q celery &
celery -A config.config_celery worker --loglevel=INFO --logfile=/code/logs/celery.log -O fair -Q celery &
sleep 5
celery -A config.config_celery.app flower --port=8002 --loglevel=INFO --logfile=/code/logs/flower.log --basic-auth=admin:admin -D &

# FastAPI Execution
if [[ $SSL_ENABLED == true ]]; then
  echo "DEBUG: Running the application on HTTPS"
  uvicorn main:app --host=0.0.0.0 --reload --port=8001 --ssl-keyfile ../certificates/certificate-key.pem --ssl-certfile ../certificates/certificate-cert.pem
else
  echo "DEBUG: Running the application on HTTP"
  uvicorn main:app --host=0.0.0.0 --reload --port=8001
fi
