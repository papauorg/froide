FROM mcr.microsoft.com/vscode/devcontainers/python:3.9-bookworm

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    binutils libproj-dev gdal-bin build-essential libmagickwand-dev libpoppler-cpp-dev npm

RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel pip-tools

COPY requirements-test.txt ./requirements-test.txt
RUN pip install -r requirements-test.txt

COPY package.json ./package.json
RUN yarn install
