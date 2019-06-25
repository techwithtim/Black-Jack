FROM gitpod/workspace-full-vnc

USER root
RUN apt-get update && apt-get install -y \
        python3-tk
