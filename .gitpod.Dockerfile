FROM gitpod/workspace-full

RUN sudo apt-get -q update && \
    sudo apt-get install chromium-chromedriver && \
    rm -rf /var/lib/apt/lists/*

USER gitpod
