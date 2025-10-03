ARG PYTHON_VERSION=3.13-slim-bookworm
FROM python:$PYTHON_VERSION AS compiler

WORKDIR /application

RUN pip install -U uv --break-system-packages &&\
    uv venv --python 3.13

ENV PATH="/application/.venv/bin:$PATH"

COPY pyproject.toml pdm.lock README.md /application/

RUN uv add pdm
ENV PDM_CHECK_UPDATE=false

RUN pdm sync --prod --no-editable

FROM python:$PYTHON_VERSION AS runner

WORKDIR /application
COPY --from=compiler /application/.venv /application/.venv

ENV PATH="/application/.venv/bin:$PATH"
# copy files
COPY src/ /application/src
COPY Jenkins/ /application/Jenkins
COPY app/ /application/app
COPY Jenkinsfile /application/
COPY Dockerfile /application/

EXPOSE 8501
EXPOSE 9999

CMD [ "python","app" ]