import functools
import os
import time


def log_file(log_name='log.txt'):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)
            with open(log_name, 'w') as log:
                log.write(output)
        return wrapper
    return deco

class Log_Process:
    def __init__(self, func):
        self.func = func
        self.logname = 'mmmm.txt'

    def __call__(self, *args, **kwargs):
        start = time.time()
        output = self.func(*args, **kwargs)
        log = open(self.logname, 'w')
        log.write(output)
        elapsed_time = time.time() - start
        print(elapsed_time)


#@log_file()
@Log_Process
def cmd():
    output = os.popen('ls -l').read()
    return output

#@log_file(log_name='another.txt')
@Log_Process
def another():
    output = os.popen("find -name '*.py'").read()
    return output

cmd()

another()
