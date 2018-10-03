FROM tensorflow/tensorflow:1.11.0-py3

RUN pip --no-cache-dir install \
        scikit-image
