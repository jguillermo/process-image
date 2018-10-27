FROM python:3.6.5-slim-jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
    python-dev \
    git \
    gcc \
    libmysqlclient-dev \
    unzip

RUN pip --no-cache-dir install \
        h5py \
        keras_applications \
        keras_preprocessing \
        pandas \
        scipy \
        sklearn \
        tensorflow \
        scikit-image

# Install Python, tools

ADD resources /resources/
RUN python --version
RUN chmod +x /resources/test.sh

WORKDIR /resources/
RUN pip install -r ./requirements.txt

WORKDIR /app

EXPOSE 80
ENTRYPOINT /resources/runservices.sh
