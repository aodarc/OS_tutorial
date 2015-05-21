__author__ = 'Alexander'
from threading import Thread, Lock
from datetime import datetime
from Lab8 import List


def f1(resource, mutex):
    mutex.acquire()
    resource.push_back(datetime.now())
    mutex.release()


def f2(resource, mutex):
    mutex.acquire()
    data, time = str(resource.pop_back()).split()
    print 'What time is it? ', time[:8]
    print 'What data today? ', data
    mutex.release()


if __name__ == "__main__":
    resource = List()
    mutex = Lock()
    p1 = Thread(target=f1, args=(resource, mutex), name="ThreadOne")
    p2 = Thread(target=f2, args=(resource, mutex), name="ThreadTwo")

    p1.start()
    p2.start()
    p1.join()
    p2.join()
