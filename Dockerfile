###########
# BUILDER #
###########
FROM ubuntu

# set work directory
WORKDIR /usr/src/elawyer-backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

#Copy requirements file to working directory
COPY requirements.txt requirements.txt

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y postgresql gcc python3-dev python3-pip python3-setuptools \
    python3-wheel musl-dev libpq-dev libtiff-dev libjpeg-dev zlib1g-dev \
    libwebp-dev tcl-dev tk-dev libharfbuzz-dev libfribidi-dev libimagequant-dev gunicorn libpng-dev \
    && pip3 install -r requirements.txt

# lint
#RUN pip install --upgrade pip
#RUN pip install flake8
#COPY . .
#RUN flake8 --ignore=E501,F401 .

# install dependencies
#COPY ./requirements.txt .
#RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/elawyer-backend/wheels -r requirements.txt

# copy entrypoint.sh
#COPY ./entrypoint.sh .

# copy project
COPY . /usr/src/elawyer-backend

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/elawyer-backend/entrypoint.sh"]
