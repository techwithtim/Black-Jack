FROM gitpod/workspace-full-vnc

USER root
RUN cd /usr/bin/
RUN apt-get install mercurial
RUN hg clone https://bitbucket.org/pygame/pygame
RUN apt-get update && apt-get install -y \
        tk-dev \
        python3-tk \
        python-tk \
        libsdl1.2-dev \
        python-pygame \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
RUN apt-get build-dep python3-pygame

