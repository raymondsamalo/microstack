import functools
from .config import huey

def exp_backoff_task(retries=10, retry_backoff=1.15):
    def deco(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            # We will register this task with `context=True`, which causes
            # Huey to pass the task instance as a keyword argument to the
            # decorated task function. This enables us to modify its retry
            # delay, multiplying it by our backoff factor, in the event of
            # an exception.
            task = kwargs.pop('task')
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                task.retry_delay *= retry_backoff
                raise exc

        # Register our wrapped task (inner()), which handles delegating to
        # our function, and in the event of an unhandled exception,
        # increases the retry delay by the given factor.
        return huey.task(retries=retries, retry_delay=1, context=True)(inner)
    return deco

from importlib import import_module

@huey.task()
def run_path_task(path, *args, **kwargs):
    path, name = path.rsplit('.', 1)  # e.g. path.to.module.function
    mod = import_module(path)  # Dynamically import the module.
    return getattr(mod, name)(*args, **kwargs)  # Call the function.

class HueyWorkerException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code