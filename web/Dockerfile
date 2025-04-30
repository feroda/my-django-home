FROM python:3.12-slim-bookworm
ENV PYTHONUNBUFFERED 1
ARG BUILD_MY_IOT_ENV=prod

RUN apt-get update && apt-get install -y lsb-release wget mosquitto build-essential gettext git wkhtmltopdf zlib1g-dev libjpeg-dev libfreetype6-dev python-dev-is-python3
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update && apt-get install -y postgresql-client unixodbc odbcinst && rm -rf /var/lib/apt/lists/*
RUN wget --quiet https://packages.microsoft.com/debian/11/prod/pool/main/m/msodbcsql18/msodbcsql18_18.2.1.1-1_amd64.deb
RUN ACCEPT_EULA=Y dpkg -i msodbcsql18_18.2.1.1-1_amd64.deb


COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install ipython
RUN pip install --no-cache-dir -r /requirements.txt

COPY requirements.dev.txt /
RUN if [ "$BUILD_MY_IOT_ENV" = "dev" ]; then pip install --upgrade --no-cache-dir -r /requirements.dev.txt; fi

WORKDIR /app
CMD ["python"]
