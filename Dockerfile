FROM python

ENV CALC_PORT=13337

COPY server.py server.py
COPY utils.py utils.py


ENTRYPOINT ["python3", "server.py"]