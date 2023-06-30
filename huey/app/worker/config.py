import logging
from logging.handlers import TimedRotatingFileHandler
from huey import RedisHuey
import os 

def create_huey():
    url = os.getenv('REDIS_URL')
    huey = RedisHuey('tasks', url=url)
    return huey

def _configure_logger():
    log_folder = os.getenv('LOG_FOLDER')
    if log_folder is not None:
        log_file_name=os.path.join(log_folder, "huey_worker.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(threadName)s %(message)s')
        handler = TimedRotatingFileHandler(log_file_name, when="midnight", backupCount=10)
        handler.setFormatter(formatter)
        logger = logging.getLogger('huey.consumer') #take logger and configure it
        logger.addHandler(handler)
        logger = logging.getLogger('huey') #take logger and configure it
        logger.addHandler(handler)

_configure_logger()
huey=create_huey()