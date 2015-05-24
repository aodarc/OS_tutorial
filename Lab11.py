__author__ = 'Alexander'
from multiprocessing import Process, Pipe

def f1(connector):
    rez = len(connector.recv().split())
    connector.send(rez)

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    server = Process(target=f1, args=(child_conn,))
    server.start()
    parent_conn.send('How many word is it?')
    print parent_conn.recv()
    server.join()
