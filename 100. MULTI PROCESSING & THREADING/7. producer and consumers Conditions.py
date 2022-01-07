import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def consumer(cv):
    logging.debug('Consumer thread started ...')
    print(cv)
    with cv:
        print(cv)
        logging.debug('Consumer waiting ...')
        cv.wait()  # Waiting will block the execution of the following code,
        # and it will wake up when other threads call notify
        logging.debug('Consumer consumed the resource')


def producer(cv):
    logging.debug('Producer thread started ...')
    print(cv)

    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()  # Notifies and wakes other threads that use the cond condition variable


if __name__ == '__main__':
    condition = threading.Condition()
    # condition.acquire()  # Lock condition variables
    # condition.release()  # UnLock condition variables
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()

    # cond = threading.Condition()  # Create a condition variable
    # cond.acquire()  # Lock condition variables

    # cond.wait()
    # print("after cond.wait()")
    # time.sleep(2)
    # cond.notify()  # Notifies and wakes other threads that use the cond condition variable
    # cond.release()
