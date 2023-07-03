#!/usr/bin/env python3
import os

import uvicorn
from a2wsgi import WSGIMiddleware

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq_dashboard import DashboardApp

REDIS_URL = os.environ.get('REDIS_URL')
REDIS_QUEUES = os.environ.get('REDIS_QUEUES', 'default')
REDIS_NAMESPACE = os.environ.get('REDIS_NAMESPACE', 'default')
PORT = int(os.environ.get('PORT', 8080))

broker = RedisBroker(url=REDIS_URL, namespace=REDIS_NAMESPACE)
for queue in REDIS_QUEUES.split(','):
    broker.declare_queue(queue)
dramatiq.set_broker(broker)

app = DashboardApp(broker=broker, prefix='')
app = WSGIMiddleware(app)
uvicorn.run(app, port=PORT, host="0.0.0.0")