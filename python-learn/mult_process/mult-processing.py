import os
from multiprocessing import Process

def run_proc(name):
    print('child process {name} {pid} Running'.format(name=name, pid=os.getpid()))

if __name__ == '__main__':
    print('Parent process {current_pid}'.format(current_pid=os.getpid()))
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print('Process will start...')
        p.start()
    p.join()
    print('Process end.')
