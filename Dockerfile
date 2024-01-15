FROM ubuntu:latest

MAINTAINER speedy


RUN apt-get -y update && apt-get install -y --no-install-recommends \
    wget \
    python3 \
    nginx \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    pip install  flask gevent gunicorn && \
    rm -rf /root/.cache



ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY model_base /opt/program
COPY run_serve.py /opt/program

COPY ./requirements.txt /opt/program/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/program/requirements.txt

WORKDIR /opt/program

EXPOSE 8080

#ENTRYPOINT ['python3', 'predictor.py']
ENTRYPOINT ["python3", "run_serve.py"]

# CMD tail -f /dev/null
