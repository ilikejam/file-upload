FROM python:3

# hadolint ignore=DL3013
RUN pip install --no-cache-dir bottle werkzeug

COPY app.py /app.py
COPY upload.htm /upload.htm

ENTRYPOINT ["/usr/local/bin/python", "/app.py"]
