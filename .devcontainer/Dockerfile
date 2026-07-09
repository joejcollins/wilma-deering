FROM mcr.microsoft.com/devcontainers/base:resolute

# Install uv for everyone not just the current user.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && cp /root/.local/bin/uv /usr/local/bin/uv

# Install updates and utilities
RUN sudo apt-get update \
    && sudo apt-get install --assume-yes python3-dev texlive-latex-extra texlive-extra-utils latexmk tex-fmt jq \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Fixed uv cache to improve the venv build time
RUN mkdir -p /opt/uv-cache
ENV UV_CACHE_DIR=/opt/uv-cache \
    UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project \
    && uv cache prune --ci
RUN chmod -R 777 /opt/uv-cache

ENV UV_CACHE_DIR=/opt/uv-cache \
    UV_LINK_MODE=copy \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Add some labels so it looks nice in Github packages.
LABEL org.opencontainers.image.source=https://github.com/joejcollins/wilma-deering/
LABEL org.opencontainers.image.description="wilma-deering image."