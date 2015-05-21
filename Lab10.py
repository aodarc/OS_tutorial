__author__ = 'Alexander'
from threading import Thread, BoundedSemaphore


class Queue:
    def __init__(self):
        self.list = []

    def push(self, elem):
        self.list.insert(0, elem)

    def pop(self):
        return self.list.pop()

    def __iter__(self):
        return self.list.__iter__()

    def __len__(self):
        return len(self.list)


def f1(q, sem):
    sem.acquire()
    q.pop()
    print len(q)
    for x in q:
        print x


if __name__ == "__main__":
    q = Queue()
    semaphore = BoundedSemaphore(value=1)

    q.push('First string')
    q.push('Hello world')
    q.push('This is last string((')

    t1 = Thread(target=f1, args=(q, semaphore))

    t1.start()
    t1.join()