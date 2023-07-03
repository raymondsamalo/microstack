import logging
from logging.handlers import TimedRotatingFileHandler
import dramatiq
import os 

from dramatiq.brokers.redis import RedisBroker

def _configure_broker():
    REDIS_URL = os.environ.get('REDIS_URL')
    REDIS_QUEUES = os.environ.get('REDIS_QUEUES', 'default')
    REDIS_NAMESPACE = os.environ.get('REDIS_NAMESPACE', 'default')
    PORT = int(os.environ.get('PORT', 8080))

    broker = RedisBroker(url=REDIS_URL, namespace=REDIS_NAMESPACE)
    for queue in REDIS_QUEUES.split(','):
        broker.declare_queue(queue)
    dramatiq.set_broker(broker)


def worker_logger():
    log_folder = os.getenv('LOG_FOLDER')
    logger = logging.getLogger('worker') #take logger and configure it
    if log_folder is not None:
        log_file_name=os.path.join(log_folder, "worker.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(threadName)s %(message)s')
        handler = TimedRotatingFileHandler(log_file_name, when="midnight", backupCount=10)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

_configure_broker()