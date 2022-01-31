"""
To use multiple processes, we create a multiprocessing Pool
 With the map method it provides, we will pass the list of URLs to the pool, which in turn will spawn eight
 new processes and use each one to download the images in parallel.
 This is true parallelism, but it comes with a cost.

The entire memory of the script is copied into each subprocess that is spawned.

 In this simple example, it isn’t a big deal, but it can easily become serious overhead for non-trivial programs.
"""

import logging
import os
from functools import partial
from multiprocessing.pool import Pool
from time import time

from tutorial_download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():

    ts = time()
    client_id = "4591084c070d7d4"
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    download = partial(download_link, download_dir)

    with Pool(4) as p:
        p.map(download, links)  # Apply `func` to each element in `iterable`

    logging.info('Took %s seconds', time() - ts)


if __name__ == '__main__':
    main()
