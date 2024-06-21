FROM python:3

RUN pip install --no-cache-dir bottle==0.12.25 werkzeug==3.0.3

COPY app.py /app.py
COPY upload.htm /upload.htm

ENTRYPOINT ["/usr/local/bin/python", "/app.py"]
