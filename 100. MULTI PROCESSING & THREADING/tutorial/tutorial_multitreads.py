"""
This module will create a pool of eight threads, making a total of nine threads including the main thread.

This is almost the same as the previous one, with the exception that we now have a new class, DownloadWorker, which is
a descendent(потомок) of the Python Thread class.
The run method has been overridden, which runs an infinite loop.
On every iteration, it calls self.queue.get() to try and fetch a URL to from a thread-safe queue.
It blocks until there is an item in the queue for the worker to process.
Once the worker receives an item from the queue, it then calls the same download_link
After the download is finished, the worker signals the queue that that task is done.
This is very important, because the Queue keeps track of how many tasks were enqueued(поставлен в очередь).
The call to queue.join() would block the main thread forever
if the workers did not signal that they completed a task.

links len = 23 Took 7.058806896209717

While this is much faster, it is worth mentioning that only one thread was executing at a time throughout this
process due to the GIL.
Therefore, this code is concurrent but not parallel.
The reason it is still faster is because this is an IO bound task.
The processor is hardly breaking a sweat while downloading these images, and the majority of the time is spent
waiting for the network. This is why Python multithreading can provide a large speed increase.
The processor can switch between the threads whenever one of them is ready to do some work.
Using the threading module in Python or any other interpreted language with a GIL can
actually result in reduced performance.  If your code is performing a CPU bound task, such as decompressing gzip files,
using the threading module will result in a slower execution time.

For CPU bound tasks and truly parallel execution, we can use the multiprocessing module.
"""
import logging
import os
from queue import Queue
from threading import Thread
from time import time

from tutorial_download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class DownloadWorker(Thread):

    def __init__(self, queue: Queue):
        Thread.__init__(self)
        self.queue = queue  # shared object between Threads in memory

    def run(self):
        logger.info(f'module name: {__name__} parent process: {os.getppid()} process id: {os.getpid()}')
        # name = __main__; parent process: 14504 is SAME; process id: 15436 is SAME
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            logger.info(f"Downloading started of {link}")

            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()


def main():
    ts = time()
    client_id = "4591084c070d7d4"
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    for x in range(8):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for link in links:
        logger.info('Queueing {}'.format(link))
        queue.put((download_dir, link))

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()  # Blocks until all items in the Queue have been gotten and processed.
    logging.info('Took %s', time() - ts)


if __name__ == '__main__':
    main()
