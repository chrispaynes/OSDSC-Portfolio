FROM local/jupyter_nb_base

RUN apt-get update \
    && pip install --upgrade pip \
    && conda install -y python=3.6

RUN pip install tensorflow
