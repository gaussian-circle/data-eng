# base docker image that we will build on
FROM python:3.13.11-slim

# copy uv binary from github
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# set up the working directory inside the container
WORKDIR /code

# add virtual environment to path
ENV PATH="/code/.venv/bin:$PATH"

# copy dependency files
COPY pyproject.toml uv.lock .python-version ./
# sync dependencies
RUN uv sync --locked

# copy the script to the workdir
COPY ingest_data.py ingest_data.py

# define what to do first when the container runs
ENTRYPOINT ["python", "ingest_data.py"]