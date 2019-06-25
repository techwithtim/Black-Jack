FROM gitpod/workspace-full-vnc

USER root
RUN apt-get update && apt-get install -y \
        tk-dev \
        python3-tk \
        python-tk \
        libsdl1.2-dev \
        python3-pygame \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

