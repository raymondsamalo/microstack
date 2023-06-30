from .config import huey

@huey.task()
def add(a, b):
    return a + b