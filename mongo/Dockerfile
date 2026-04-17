FROM mongo:7.0

USER root

COPY --chown=mongodb:mongodb ./init /docker-entrypoint-initdb.d

RUN mkdir -p /data/db /data/configdb \
    && chown -R mongodb:mongodb /data/db /data/configdb /docker-entrypoint-initdb.d

USER mongodb
