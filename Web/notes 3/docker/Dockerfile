FROM openjdk:8-jdk

COPY app.jar /app/
COPY flag.sh /flag.sh
COPY notes /notes

ENV FLAG "CBCTF{test_flag}"

RUN ls /notes && \
    chmod -R 777 /notes &&\
    useradd -m -s /bin/bash ctfer && \
    chmod 700 /flag.sh

CMD ["/bin/bash", "-c", "/flag.sh && exec su ctfer -c 'java -jar /app/app.jar'"]

EXPOSE 12345
