FROM python:3.6.5-slim-jessie

RUN apt-get update && apt-get install -y --no-install-recommends

RUN pip install --upgrade pip

ADD resources /resources/
RUN python --version
RUN chmod +x /resources/test.sh

WORKDIR /resources/
RUN pip install -r ./requirements.txt

WORKDIR /app

EXPOSE 80
ENTRYPOINT /resources/runservices.sh
