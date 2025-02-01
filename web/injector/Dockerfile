FROM python:3.12

WORKDIR /app

COPY challenge /app

RUN pip install --no-cache-dir -r /app/requirements.txt \
    && adduser --disabled-password --gecos "" ctf \
    && chown -R ctf:ctf /app

USER ctf

EXPOSE 1337

CMD ["flask", "run", "--host=0.0.0.0", "--port=1337"]
