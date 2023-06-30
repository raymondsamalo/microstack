from huey import RedisHuey
import os 
_password = os.environ['REDIS_PASSWORD']
huey = RedisHuey('testing', password=_password)
