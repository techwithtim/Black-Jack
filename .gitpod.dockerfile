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
        python3-dev \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
RUN apt-get build-dep pygame
RUN cd pygame
RUN python3 config.py
RUN python3 setup.py build
RUN sudo python3 setup.py install
