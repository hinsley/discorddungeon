FROM gitpod/workspace-full

RUN sudo apt-get -q update && \
    sudo apt-get install -yq chromium-browser && \
    rm -rf /var/lib/apt/lists/*

USER gitpod
