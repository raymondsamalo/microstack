#!/usr/bin/env python3

from app.worker.config import huey
from app.worker.tasks import add
if __name__ == '__main__':
    result = add(1, 2)
    print('1 + 2 = %s' % result.get(blocking=True))