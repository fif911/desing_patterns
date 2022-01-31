"""
Python concurrent.futures

This package provides yet another way to use concurrency and parallelism with Python.

Using a concurrent.futures.ThreadPoolExecutor makes the Python threading example code almost
identical to the multiprocessing module.
"""

import logging
import os
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import time

from tutorial_download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def main():
    client_id = "4591084c070d7d4"
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)

    # By placing the executor inside a with block, the executors shutdown method
    # will be called cleaning up threads.
    #
    # By default, the executor sets number of workers to 5 times the number of
    # CPUs.
    with ThreadPoolExecutor() as executor:
        # Create a new partially applied function that stores the directory
        # argument.
        #
        # This allows the download_link function that normally takes two
        # arguments to work with the map function that expects a function of a
        # single argument.
        fn = partial(download_link, download_dir)

        # Executes fn concurrently using threads on the links iterable. The
        # timeout is for the entire process, not a single call, so downloading
        # all images must complete within 30 seconds.
        executor.map(fn, links, timeout=30)
        logger.info("After executor.map")


if __name__ == '__main__':
    main()
