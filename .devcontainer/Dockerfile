ARG BUILDPLATFORM=linux/amd64
FROM --platform=${BUILDPLATFORM} ubuntu:22.04
ARG IMAGE_NAME=pennlabs/courses-devcontainer
RUN apt-get update && apt-get install -y wget curl gcc python3-dev libpq-dev postgresql-client