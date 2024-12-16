# Use an official Python runtime as an image
FROM python:3.6


EXPOSE 5000


WORKDIR /app

COPY ./* /app/

COPY templates /app/templates

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install -U pip

RUN pip install -r requirements.txt
RUN chmod +x start.sh

ENV FLAG "CBCTF{test_flag}"

CMD ["./start.sh"]
