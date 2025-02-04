FROM python:3.12

WORKDIR /app
COPY ./challenge .

RUN pip3 install -r requirements.txt

EXPOSE 1337

CMD ["flask", "run", "--host=0.0.0.0", "--port=1337"]
