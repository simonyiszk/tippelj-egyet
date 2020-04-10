FROM python:3

COPY . /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app

EXPOSE 5000
EXPOSE 8765

CMD ./run.sh
