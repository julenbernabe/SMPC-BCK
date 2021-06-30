FROM ubuntu:18.04

WORKDIR /root

# Install required packages
RUN apt-get update && apt-get install -y \
  bzip2 \
  curl \
  doxygen \
  g++ \
  gcc \
  git \
  libcrypto++-dev \
  libgmp3-dev \
  libssl-dev \
  m4 \
  make \
  patch \
  python \
  python3 \
  vim \
  wget \
  yasm \
  zip \
  nano \
  net-tools \
  iputils-ping \
  python3-pip

ADD install_dependencies.sh .
RUN ["bash", "install_dependencies.sh"]

COPY ./SCALE-MAMBA /root/SCALE-MAMBA

ADD source/ /root/source
ADD install.sh .
RUN ["bash", "install.sh"]

COPY ./data-scientist-eth-client/requirements.txt /root
RUN pip3 install -r requirements.txt

ENV PATH ~/.cargo/bin/:${PATH}

EXPOSE 5001

CMD ["/bin/bash"]
