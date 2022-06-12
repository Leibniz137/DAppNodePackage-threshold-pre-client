FROM nucypher/nucypher:v6.1.0@sha256:4a1d3ba4a1a1e5803af1bb7bc016770870a9158aa140ba0f59ac651b2ce4d42b

WORKDIR /usr/src/app

RUN pip3 install web3

COPY src/entrypoint.sh ./entrypoint.sh
COPY src/init.py ./init.py

ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]
