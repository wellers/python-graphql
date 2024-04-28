FROM python:3.12.1-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "-u", "src/app.py" ]