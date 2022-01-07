"""
technique for inter-process communication
https://docs.python.org/3/library/threading.html#threading.Event

multiprocessing.Event SAME AS threading.Event
Class implementing event objects.

An event manages a flag that can be set to true with the set() method and reset to false with the clear() method.
"""
import multiprocessing
import time


def worker(event):
    print(f"started worker at {time.time()}")
    time.sleep(1)
    print(f"finished worker at {time.time()}")
    event.set()


if __name__ == '__main__':
    event = multiprocessing.Event()

    process = multiprocessing.Process(
        target=worker, args=[event])
    process.start()
    print(f"started process at {time.time()}")
    event.wait()  # The wait() method blocks until the flag is true. The flag is initially false.
    print("finished main thread")
