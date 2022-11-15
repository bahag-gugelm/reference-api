# Dockerfile
FROM python:3.9

WORKDIR /opt/utils_api

# setting up the virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copying the project files
COPY . /opt/utils_api

# needed to prevent from breaking on rfc6266 install
RUN pip install setuptools==57.5.0
# installing reqs
RUN pip install -r requirements.txt

EXPOSE 8000

CMD exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
