FROM python:3.9-slim-bullseye AS base
RUN apt-get update
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS dev
RUN pip install ptvsd debugpy
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

FROM base AS test
# Install pytest
RUN pip install pytest

FROM base AS prod
COPY . .
CMD ["python", "-m", "commands", "to", "run", "app"]



