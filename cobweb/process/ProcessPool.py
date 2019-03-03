import os
import random
import time
from multiprocessing import Pool


def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end' % name)


if __name__ == '__main__':
    print('current process %s.' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('waiting for all subProcesses done...')
    p.close()
    p.join()
    print('All subProcess done')
