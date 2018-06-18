FROM ubuntu:16.04

ENV BUILD_PACKAGES="build-essential pkg-config libcurl3-gnutls-dev libc6-dev libevent-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python zlib1g-dev curl wget bsdmainutils automake libboost-all-dev libssl-dev libprotobuf-dev protobuf-compiler libqt4-dev libqrencode-dev libdb++-dev"

RUN apt update && \
    apt install -y $BUILD_PACKAGES

COPY fetch-params.sh .
RUN ./fetch-params.sh

LABEL komodo_version="0.0605a"

RUN git clone https://github.com/jl777/komodo

#COPY *.tar.* /komodo/depends/sources/ 

RUN cd komodo && \
    git checkout jl777 && \
    ./zcutil/fetch-params.sh && \
    ./zcutil/build.sh -j$(nproc)

RUN apt remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /komodo/depends

RUN apt update && apt install -y libcurl3-gnutls-dev libgomp1 telnet curl

RUN useradd -u 3003 -m komodo && \
    mv /root/.zcash-params /home/komodo/ && \
    chown -R komodo:komodo /home/komodo/.zcash-params

ENV PATH="/komodo/src/:${PATH}"
USER komodo
WORKDIR /home/komodo

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
