from multiprocessing import Process, Queue
import os, time, random


#write data to Process
def proc_write(q, urls):
    print('Process {pid} is writing...'.format(pid=os.getpid()))
    for url in urls:
        q.put(url)
        print('Put {url} to queue...'.format(url=url))
        time.sleep(random.random())


# read data to Process
def proc_read(q):
    print('Process {pid} is reading...'.format(pid=os.getpid()))
    while True:
        url = q.get(True)
        print('Get {url} from queue...'.format(url=url))


if __name__ == '__main__':
    # father process create queue , tranform to each child Process
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))

    # start child Process, write
    proc_write1.start()
    proc_write2.start()

    # start child Process, reading
    proc_reader.start()
    # waiting proc_write end
    proc_write1.join()
    proc_write2.join()

    # forcore end
    proc_reader.terminate()
