"""
If you’re using Python 3.8 or newer, then you can use the new shared_memory module to more effectively
share data across Python processes

This small program creates a list of 100 characters and modifies the first 50 from another process.

Notice only the name of the buffer is passed to the second process. Then the second process can retrieve that same
block of memory using the unique name. This is a special feature of the shared_memory module that’s powered by mmap.
Under the hood, the shared_memory module uses each operating system’s unique API to create named memory maps for you.
"""

from multiprocessing import Process
from multiprocessing import shared_memory


def modify(buf_name):
    shm = shared_memory.SharedMemory(buf_name)
    shm.buf[0:50] = b"b" * 50
    shm.close()


if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=100)

    try:
        shm.buf[0:100] = b"a" * 100
        proc = Process(target=modify, args=(shm.name,))
        proc.start()
        proc.join()
        print(bytes(shm.buf[:100]))
    finally:
        shm.close()
        shm.unlink()
