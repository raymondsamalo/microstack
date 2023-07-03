FROM python:3.10-slim
COPY requirements.txt requirements.txt
COPY app app
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "dramatiq","app.worker" ]