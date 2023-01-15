FROM ubuntu:18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    cmake \
    curl \
    git \
    libcurl3-dev \
    libleptonica-dev \
    liblog4cplus-dev \
    libopencv-dev \
    libtesseract-dev \
    wget \
    python3 \
    python3-distutils

WORKDIR /app

COPY . .

RUN mkdir /app/openalpr/src/build && \
    cd /app/openalpr/src/build && \
    cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc .. && \
    make && \
    make install

RUN cd /app/openalpr/src/bindings/python && \
    python3 setup.py install

entrypoint ["python3", "main.py"]

