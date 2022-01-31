"""
https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

On my laptop, this script took 19.4 seconds to download 91 images. Please do note that these numbers may vary based on
the network you are on. 19.4 seconds isn’t terribly long, but what if we wanted to download more pictures? Perhaps 900
images, instead of 90. With an average of 0.2 seconds per picture, 900 images would take approximately 3 minutes.
For 9000 pictures it would take 30 minutes. The good news is that by introducing concurrency or parallelism,
we can speed this up dramatically.

links len = 18 Took 16.20571494102478 seconds
"""

import logging
import os

from time import time

from tutorial_download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    ts = time()
    client_id = "4591084c070d7d4"
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)

    for link in links:
        download_link(download_dir, link)
    logging.info('Took %s seconds', time() - ts)


if __name__ == '__main__':
    main()
