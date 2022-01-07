"""
Distributing to Multiple Workers (Multiple remote machines that perform tasks from one queue)

While the threading and multiprocessing modules are great for scripts that are running on your personal computer,
what should you do if you want the work to be done on a different machine, or you need to scale up to more than
the CPU on one machine can handle?
    A great use case for this is long-running back-end tasks for web applications.
    If you have some long-running tasks, you don’t want to spin up a bunch of sub-processes or threads on the same
    machine that need to be running the rest of your application code.
    ( This will degrade the performance of your application for all of your users.)
    What would be great is to be able to run these jobs on another machine, or many other machines.

A great Python library for this task is RQ, a very simple yet powerful library.
You first enqueue a function and its arguments using the library.
This pickles the function call representation, which is then appended to a Redis list.
Enqueueing the job is the first step, but will not do anything yet.
We also need at least one worker to listen on that job queue.


instead of just calling our download_link method, we call q.enqueue(download_link, download_dir, link)
he enqueue method takes a function as its first argument, then any other arguments or keyword arguments
are passed along to that function when the job is actually executed.

One last step we need to do is to start up some workers. RQ provides a handy script to run workers on the default queue.
Just run rqworker in a terminal window and it will start a worker listening on the default queue.

The great thing about RQ is that as long as you can connect to Redis, you can run as many workers as you like on as
many different machines as you like; therefore, it is very easy to scale up as your application grows.

However, RQ is not the only Python job queue solution. RQ is easy to use and covers simple use cases extremely well,
but if more advanced options are required, other Python 3 queue solutions (such as Celery) can be used.
"""

import logging
import os

from redis import Redis

from rq import Queue

from tutorial_download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    client_id = "4591084c070d7d4"
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    q = Queue(connection=Redis(host='localhost', port=6379))
    for link in links:
        q.enqueue(download_link, download_dir, link)


if __name__ == '__main__':
    main()
