FROM nucypher/nucypher:v6.0.0@sha256:850449ef09ba1902b5fd9bb698d233d8d708cda53bf016c6e1e58fc6cc3a9527

WORKDIR /usr/src/app

COPY src/entrypoint.sh ./entrypoint.sh
COPY src/init.py ./init.py

ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]
