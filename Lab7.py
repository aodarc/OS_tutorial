# coding: utf-8
__author__ = 'Alexander'
from multiprocessing import Process
from random import random
import os


def f(name):
    print "Process id: ", os.getpid(), name
    matrix = [[int(random()*10) for i in xrange(5)] for x in xrange(5)]
    elem_set = set()
    for arr in matrix:
        elem_set.update(set(arr))
    elem_set = {kay: 0 for kay in elem_set}
    for row in matrix:
        for elem in row:
            elem_set[elem] += 1
    print elem_set, '\n'

    client_bunk = {
        'time':                  ['2015.05.11', '2014.11.14', '2015.09.24'],
        'first_name':            ['Alex',       'Carry',      'Max'],
        'second_name':           ['Master',     'Killer',     'Mud'],
        'id':                    [12445,        35487,        10777],
        'sum_of_transfer_money': [37.95,        99.45,        101.2]
    }

    p2 = Process(target=f2, args=(f2, client_bunk))
    p2.start()
    p2.join()


def f2(name, client):
    print "Process id: ", os.getpid(), name
    index = client['time'].index('2015.09.24')
    for n, info in zip(client.keys(), client.values()):
        print n, info[index]

if __name__ == '__main__':
    p = Process(target=f, args=(f,))
    p.start()
    p.join()

