import os

if __name__ == '__main__':
    print('current Process {pid} start...'.format(pid=os.getpid()))
pid = os.fork()
if pid < 0:
    print('error in fork')
elif pid == 0:
    print('I am child process {pid} and my parent process is {ppid}'.format(pid=os.getpid(), ppid=os.getppid()))
else:
    print('I {ppid} created a child process {pid}.'.format(ppid=os.getpid(), pid=pid) )
