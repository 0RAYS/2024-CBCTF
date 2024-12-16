FROM openjdk:8-jdk

COPY Client.jar /app/
COPY flag.sh /flag.sh

ENV FLAG "only_within_a_flash_of_thought}"

RUN useradd -m -s /bin/bash ctfer && \
    chmod 700 /flag.sh

CMD ["/bin/bash", "-c", "/flag.sh && exec su ctfer -c 'java -jar /app/Client.jar'"]

EXPOSE 12345
