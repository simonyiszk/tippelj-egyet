FROM python:3

COPY . /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app
RUN find assets/ ! -name style.css ! -name impresszum.html -type f -exec convert -resize 'x600' {} {}  \;

EXPOSE 5000
EXPOSE 8765

CMD ./run.sh
