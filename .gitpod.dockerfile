FROM gitpod/workspace-full-vnc

USER root
RUN sudo apt-get install python3-tk tk
RUN sudo apt-get install tk-dev
