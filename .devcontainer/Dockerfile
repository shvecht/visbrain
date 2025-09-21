# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies if needed in future; placeholder for apt-get usage
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
    && rm -rf /var/lib/apt/lists/*

# Default workdir handled by devcontainer tooling
