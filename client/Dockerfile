FROM python:3.10.3-bullseye

ENV APP_HOME /app
ENV MP_SPDZ_HOME $APP_HOME/MP-SPDZ

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
                automake \
                build-essential \
                clang-11 \
                git \
                libboost-dev \
                libboost-thread-dev \
                libclang-dev \
                libntl-dev \
                libsodium-dev \
                libssl-dev \
                libtool \
                m4 \
                texinfo \
                yasm \
                vim \
                gdb \
                valgrind \
        && rm -rf /var/lib/apt/lists/*

# mpir
COPY --from=initc3/mpir:55fe6a9 /usr/local/mpir/include/* /usr/local/include/
COPY --from=initc3/mpir:55fe6a9 /usr/local/mpir/lib/* /usr/local/lib/
COPY --from=initc3/mpir:55fe6a9 /usr/local/mpir/share/info/* /usr/local/share/info/

WORKDIR $MP_SPDZ_HOME

RUN pip install --upgrade pip ipython

RUN git clone https://github.com/data61/MP-SPDZ .
RUN git checkout 5ab8c702dde2f25ae7f2f2d0e4d47f5d716fa621

COPY ./requirements.txt /app/MP-SPDZ
RUN pip install -r requirements.txt

ARG arch=native
ARG cxx=clang++-11
ARG use_ntl=0
ARG prep_dir="Player-Data"
ARG ssl_dir="Player-Data"

RUN echo "ARCH = -march=${arch}" >> CONFIG.mine \
        && echo "CXX = ${cxx}" >> CONFIG.mine \
        && echo "USE_NTL = ${use_ntl}" >> CONFIG.mine \
        && echo "MY_CFLAGS += -I/usr/local/include" >> CONFIG.mine \
        && echo "MY_LDLIBS += -Wl,-rpath -Wl,/usr/local/lib -L/usr/local/lib" \
            >> CONFIG.mine \
        && mkdir -p $prep_dir $ssl_dir \
        && echo "PREP_DIR = '-DPREP_DIR=\"${prep_dir}/\"'" >> CONFIG.mine \
        && echo "SSL_DIR = '-DSSL_DIR=\"${ssl_dir}/\"'" >> CONFIG.mine

# ssl keys
ARG cryptoplayers=0
ENV PLAYERS ${cryptoplayers}
RUN ./Scripts/setup-ssl.sh ${cryptoplayers} ${ssl_dir}


# Dishonest Majority protocols
RUN make -j8 mascot-party.x
RUN make -j8 temi-party.x

# Honest Majority protocols
RUN make -j8 malicious-shamir-party.x

ENTRYPOINT ["tail", "-f", "/dev/null"]
