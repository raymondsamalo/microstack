import logging
import os
from subprocess import Popen, PIPE, STDOUT
from typing import List
from .config import huey
from .utils import HueyWorkerException, exp_backoff_task


def _script(script_name: str, args: List[str], check_exitcode: bool = True, task=None):
    logger = logging.getLogger('huey')  # take logger and configure it
    script_path = os.path.join('/scripts', script_name)
    commands = [script_path]
    commands.extend(args)
    command_string = ' '.join(commands)
    if task is not None:
        command_uuid = task.id
    else:
        command_uuid =  ""
    logger.info('[%s] [run commands] %s', command_uuid, command_string)
    process = Popen(commands, stdout=PIPE, stderr=STDOUT)
    with process.stdout:
        for line in process.stdout:
            logger.info("[%s] [out] %s", command_uuid, line.decode())
    exitcode = process.wait()  # 0 means success    logging.info(result.)
    logger.info("[%s] [completed with] %d", command_uuid, exitcode)
    if check_exitcode and exitcode != 0:
        raise HueyWorkerException(
            f"script {command_string} return {exitcode}", exitcode)


@exp_backoff_task(retries=5, retry_backoff=2)
def script_backoff(script_name: str, args: List[str] = [], check_exitcode: bool = True, task=None):
    _script(script_name, args, check_exitcode=check_exitcode, task=task)


@huey.task(retries=2,context=True)
def script_retry(script_name: str, args: List[str] = [], check_exitcode: bool = True, task=None):
    _script(script_name, args, check_exitcode=check_exitcode, task=task)


@huey.task(context=True)
def script_run(script_name: str, args: List[str] = [], check_exitcode: bool = True, task=None):
    _script(script_name, args, check_exitcode=check_exitcode, task=task)
