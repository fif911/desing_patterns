import threading
import time

DEAD_LOCK = 1

if __name__ == '__main__':

    first = threading.Lock()  # it's unlocked by default
    second = threading.Lock()  # it's unlocked by default
    print(f"first: {first}")
    print(f"second: {second}")

    first.acquire()
    # second.acquire()
    # second.release()  # You cannot release unlocked lock

    while True:
        time.sleep(1)

        print(f"first: {first}")
        print(f"second: {second}")

        print(first.locked())
        print(second.locked())
        if first.locked():
            first.release()
            second.acquire()
            continue
        if second.locked():
            first.acquire()
            if DEAD_LOCK:
                print("Right before the DEADLOCK")
                print(f"first: {first}")
                print(f"second: {second}")
                first.acquire()  # WILL CREATE A DEADLOCK
            second.release()
            continue
