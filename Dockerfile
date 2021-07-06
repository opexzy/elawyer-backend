###########
# BUILDER #
###########
FROM ubuntu:20.04

# pull official base image
FROM python:3.8.3

# set work directory
WORKDIR /usr/src/elawyer-backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y postgresql gcc python3-dev musl-dev libffi-dev tiff jpeg openjpeg zlib freetype lcms2 \
    libwebp-dev tcl-dev tk-dev harfbuzz fribidi libimagequant-dev gunicorn \
    libxcb libpng-dev

# lint
#RUN pip install --upgrade pip
#RUN pip install flake8
#COPY . .
#RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/elawyer-backend/wheels -r requirements.txt

# copy entrypoint.sh
#COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/elawyer-backend/entrypoint.sh"]
