import threading
import time
import random


# 自定义自己 thread_learn 类，集成 threading.Thread 类
class MyThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('current %s is running...' % threading.current_thread().name)
        for url in self.urls:
            print('%s --->>> %s' % (threading.current_thread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)


mylock = threading.RLock()
num = 0


class MyThreadLock(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('{thread_name} locked, Number: {num}'.format(thread_name=threading.current_thread().name, num=num))
            if num > 4:
                mylock.release()
                print('{thread_name} released, Number: {num}'.format(thread_name=threading.current_thread().name, num=num))
                break

            num += 1
            print('{thread_name} released, Number: {num}'.format(thread_name=threading.current_thread().name, num=num))
            mylock.release()


if __name__ == '__main__':
    print('%s is running...' % threading.current_thread().name)

    # thread1 = MyThreadLock('thread_1')
    # thread2 = MyThreadLock('thread_2')
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()

    t1 = MyThread(name='thread_1', urls=['url1', 'url2', 'url3'])
    t2 = MyThread(name='thread_2', urls=['url4', 'url5', 'url6'])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('%s ended.' % threading.current_thread().name)
