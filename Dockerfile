ARG PYTHON_VERSION=3.13-slim-bookworm
FROM python:$PYTHON_VERSION AS compiler

USER root

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /application

COPY src/ /application/src
COPY Jenkins/ /application/Jenkins
COPY app/ /application/app
COPY Jenkinsfile /application/
COPY Dockerfile /application/

RUN pip install -U uv &&\
    uv venv --python 3.13

RUN . .venv/bin/activate

ENV PATH="/application/.venv/bin:$PATH"

COPY pyproject.toml pdm.lock README.md /application/

RUN uv add pdm
ENV PDM_CHECK_UPDATE=false

RUN pdm install --prod --no-editable

EXPOSE 8501
EXPOSE 9999

CMD [ "python","app" ]