from multiprocessing import Process, Lock

import time

def f(l, i):
    l.acquire()
    print 'hello world', i
    time.sleep(2)
    print "new line ", i
    l.release()

if __name__ == '__main__':
    lock = Lock()

    proc_list = [Process(target=f, args=(lock, num)) for num in range(10)]
    map(lambda x: x.start(), proc_list)
    map(lambda x: x.join(), proc_list)

