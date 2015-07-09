'''
control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
'''
from random import randrange
from string import ascii_letters
from timeit import timeit
from multiprocessing import Queue
from multiprocessing import JoinableQueue
from output import OutThread
from worker import WorkerThread


def randomstring(length=1000):
    '''
    generates a random string of alphabetic
    characters of length one thousand
    '''
    res = []
    for i in range(length):
        res.append(ascii_letters[randrange(len(ascii_letters))])
    return ''.join(res)


def run():
    WORKERS = 10

    inq = JoinableQueue(maxsize=int(WORKERS * 1.5))
    outq = Queue(maxsize=int(WORKERS * 1.5))

    ot = OutThread(WORKERS, outq)
    ot.start()

    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    instring = randomstring()
    # put work on the queue
    for work in enumerate(instring):
        inq.put(work)
    # terminate the process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")

if __name__ == "__main__":
    print("Program runtime: ", timeit(
        "run()", "from __main__ import run", number=1))