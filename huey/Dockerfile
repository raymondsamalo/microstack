FROM python:3.10-slim
COPY requirements.txt requirements.txt
COPY app app
COPY worker.sh worker.sh
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "/worker.sh","-w","8","--no-periodic" ]