FROM continuumio/anaconda3

EXPOSE 8888

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

RUN conda install -y jupyter \
    numpy \
    pandas \
    scipy \
    matplotlib \
    seaborn

COPY ./docker/anaconda3/kernel.json /usr/local/share/jupyter/kernels/python3/kernel.json

WORKDIR /notebook

CMD [ "sh", "-c", "jupyter notebook --ip=0.0.0.0 --allow-root" ]
