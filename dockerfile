FROM python:3.10-slim AS requirements_builder

WORKDIR /app

RUN pip install -U pip
RUN pip install pipenv
COPY Pipfile .
RUN pipenv lock -r > requirements.prod.txt
RUN pipenv lock -d -r > requirements.dev.txt

################################################################

FROM python:3.10-slim as e2e_tests

WORKDIR /app

RUN pip install -U pip
COPY --from=requirements_builder /app/requirements.dev.txt .
RUN pip install -r requirements.dev.txt
RUN mkdir data

COPY . .

################################################################

FROM python:3.10-slim as prod

WORKDIR /app

RUN pip install -U pip
COPY --from=requirements_builder /app/requirements.prod.txt .
RUN pip install -r requirements.prod.txt
RUN mkdir data

COPY src src

CMD python /app/src/main.py