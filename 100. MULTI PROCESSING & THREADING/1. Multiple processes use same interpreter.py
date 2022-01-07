import sys
from multiprocessing import Process
import os


def info(title):
    print(title)
    print(sys.executable)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    print(sys.executable)
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
