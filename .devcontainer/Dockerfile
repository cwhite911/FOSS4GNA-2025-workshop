# Start from the official GRASS GIS development image (main branch)
FROM osgeo/grass-gis:main-ubuntu_wxgui

# Set noninteractive frontend for smoother apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools and useful dev dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    vim \
    nano \
    curl \
    wget \
    make \
    cmake \
    python3 \
    python3-pip \
    python3-grass \
    python3-numpy \
    python3-rich \
    python3-matplotlib \
    python3-pyproj \
    python3-pandas \
    python3-shapely \
    python3-yaml \
    python3-pytest \
    && rm -rf /var/lib/apt/lists/*

# Optional: Pre-install Jupyter if you want to use notebooks
RUN pip install jupyterlab ipywidgets

# Create workshop directory
WORKDIR /workspaces/grass-addon-workshop

# Default entry point
CMD ["/bin/bash"]
