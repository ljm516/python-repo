import os
from multiprocessing import Process


def create_thread_for_windows(name):
    print('child process %s (%s) Running...' % (name, os.getpid()))


def create_thread_for_unix():
    pid = os.fork()  # 使用与 unix 和了Linux 系统
    if pid < 0:
        print('error fork')

    elif pid == 0:
        print('I am child process (%s) and my parent process is (%s)', (os.getpid(), os.getppid()))
    else:
        print('I (%s) created a child process (%s).', os.getpid(), pid)


if __name__ == '__main__':
    print('current process (%s) start ...' % (os.getpid()))
    # create_thread_for_unix()
    for i in range(5):
        p = Process(target=create_thread_for_windows, args=(str(i),))
        print('Process will start.')
        p.start()
    p.join()

    print('Process end...')
