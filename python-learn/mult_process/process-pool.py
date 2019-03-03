import os
import random
import time
from multiprocessing import Pool


def run_task(name):
    print('Task {task_name} (pid={pid}) is Running...'.format(task_name=name, pid=os.getpid()))
    time.sleep(random.randm() * 3)
    print('Task {task_name} end.'.format(task_name=name))


if __name__ == '__main__':

    print('Current process {pid}'.format(pid=os.getpid()))
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('waiting for all subprocess done....')
    p.close()
    p.join()
    print('All subprocesses done')
