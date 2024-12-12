FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y python3 python3-pip

ENV CALC_PORT=value

COPY server.py server.py
COPY utils.py utils.py

ENTRYPOINT ["python3", $CALC_PORT]