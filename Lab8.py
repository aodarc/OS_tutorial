# coding: utf-8
__author__ = 'Alexander'

from threading import Thread

class List:
    def __init__(self):
        self.list = []

    def push_back(self, elem):
        self.list.append(elem)

    def push_front(self, elem):
        self.list.insert(0, elem)

    def pop_back(self):
        return self.list.pop()

    def pop_front(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

    def __iter__(self):
        return self.list.__iter__()

def clean(list):
    i = list.size()
    while i != 0:
        string = list.pop_back()
        for symbol in string:
            if symbol.isdigit():
                list.push_front(string)
                i -= 1
                break


def cipher(list):
    i = list.size()
    while i != 0:
        string = ''
        for symbol in list.pop_back():
            if symbol.isdigit():
                string += str(int(symbol) * 2)
            else:
                string += symbol
        list.push_front(string)
        i -= 1

if __name__ == "__main__":
    l = List()
    l.push_back('This string is not empty')
    l.push_front('I have magic number: 21')
    l.push_back('\nbla-bla-bla, i like number 21. Whats time? 15:31')
    l.push_front('7 5 8 54 3 1')

    t1 = Thread(target=clean, args=(l,))
    t2 = Thread(target=cipher, args=(l,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    for x in l:
        print x
