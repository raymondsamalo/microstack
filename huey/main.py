#!/usr/bin/env python3

from app.worker.config import huey
from app.worker.tasks import script_run, script_retry, script_backoff
if __name__ == '__main__':
    script_run("test.sh")
    script_retry("test.sh")
    script_backoff("test.sh")
