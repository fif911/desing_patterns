"""
To show the individual process IDs involved, here is an expanded example:
BUT SAME Python executable (python.exe)

Outcome: I can run different programs in same python interpreter
to do it:
open 2 cmd console tabs. Type "python"
Program:
import sys, time, os
print('sys.executable', sys.executable) # show current python interpreter
print('module name:', __name__) # __main__
print('process id:', os.getpid()) # different pid
print('parent process:', os.getppid())  # different pid
while True:
    print(time.time()) # can run in the same time on same python interpreter
"""

import sys
from multiprocessing import Process
import os


def info(title):
    print(title)
    print(sys.executable)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("-" * 30)


def f(name):
    print('hello', name)
    info('function f')


if __name__ == '__main__':
    print(sys.executable)  # C:\Users\ozakotianskyi\...\desing_patterns\venv\Scripts\python.exe

    info('main line Process')
    p1 = Process(target=f, args=('process 1',))
    # p2 = Process(target=f, args=('process 2',))
    p1.start()
    p1.join()

    # p2.start()
    # p2.join()
