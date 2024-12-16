FROM openjdk:8-jdk

COPY Server.jar /app/
COPY flag.sh /flag.sh
RUN mkdir -p /tmp/classes/org/example
COPY Ocean.class /tmp/classes/org/example/

ENV FLAG "CBCTF{heaven_and_hell_is_"

RUN chmod -R 777 /tmp/classes && \
    useradd -m -s /bin/bash ctfer && \
    chmod 700 /flag.sh

CMD ["/bin/bash", "-c", "/flag.sh && exec su ctfer -c 'java -jar /app/Server.jar'"]

EXPOSE 12345
