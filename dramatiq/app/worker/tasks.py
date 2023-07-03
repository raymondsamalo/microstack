import os
from subprocess import Popen, PIPE, STDOUT
from typing import List
import uuid
import dramatiq
from .config import worker_logger
class WorkerException(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

def _script(script_name: str, args: List[str], check_exitcode: bool = True):
    logger = worker_logger()  # take logger and configure it
    script_path = os.path.join('/scripts', script_name)
    commands = [script_path]
    commands.extend(args)
    command_string = ' '.join(commands)
    command_uuid = uuid.uuid1()
    logger.info('[%s] [run commands] %s', command_uuid, command_string)
    process = Popen(commands, stdout=PIPE, stderr=STDOUT)
    with process.stdout:
        for line in process.stdout:
            logger.info("[%s] [out] %s", command_uuid, line.decode())
    exitcode = process.wait()  # 0 means success    logging.info(result.)
    logger.info("[%s] [completed with] %d", command_uuid, exitcode)
    if check_exitcode and exitcode != 0:
        raise WorkerException(
            f"script {command_string} return {exitcode}", exitcode)



@dramatiq.actor
def script_run(script_name: str, args: List[str] = [], check_exitcode: bool = True):
    _script(script_name, args, check_exitcode=check_exitcode)
