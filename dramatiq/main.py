#!/usr/bin/env python3

from app.worker.tasks import script_run
if __name__ == '__main__':
    script_run.send("test.sh")