FROM python:3.11

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install poetry

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

RUN poetry install
