FROM php:7.1-apache

COPY src/ /var/www/html/
COPY flag.sh /flag.sh

ENV FLAG "CBCTF{test_flag}"
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html &&\
    chmod +x /flag.sh &&\
    mkdir /notes && chmod -R 777 /notes


COPY note3.txt /notes
COPY note4.txt /notes
EXPOSE 80
CMD ["/bin/bash","-c","/flag.sh && apache2-foreground"]
