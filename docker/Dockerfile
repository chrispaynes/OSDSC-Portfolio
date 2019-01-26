FROM continuumio/anaconda3

EXPOSE 8888

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/*

# core packages
RUN conda install -y jupyter
RUN conda install -y numpy
RUN conda install -y pandas
RUN conda install -y matplotlib
RUN conda install -y scikit-learn
RUN conda install -y scipy
RUN conda install -y dask

COPY ./anaconda3/kernel.json /usr/local/share/jupyter/kernels/python3/kernel.json
RUN jupyter notebook --generate-config
COPY ./anaconda3/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

WORKDIR /notebook

CMD [ "sh", "-c", "jupyter notebook --ip=0.0.0.0 --allow-root" ]
