FROM anaconda/miniconda:latest

# Accept ToS via environment variable
ENV CONDA_PLUGINS_AUTO_ACCEPT_TOS=true

RUN apt-get update && apt-get install -y \
    curl \
    gitg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN conda install -c conda-forge gdal