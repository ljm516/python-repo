import random
import threading
import time


def thread_run(urls):
    print('current %s is running...' % threading.current_thread().name)
    for url in urls:
        print('%s --->>> %s' % (threading.current_thread().name, url))
        time.sleep(random.random())


if __name__ == '__main__':
    print('%s is running...' % threading.current_thread().name)
    t1 = threading.Thread(target=thread_run, name='thread_1', args=(['url1', 'url2', 'url3'], ))
    t2 = threading.Thread(target=thread_run, name='thread_2', args=(['url4', 'url5', 'url6'], ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('%s ended.' % threading.current_thread().name)
