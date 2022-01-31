"""
Python 3’s asyncio module
Compared to the other examples, there is some new Python syntax

The first new thing we do with the asyncio module is to obtain the event loop.
The event loop handles all of the asynchronous code.
Then, the loop is run until complete and passed the main function.
The async def syntax marks a function as a coroutine (Сопрограмма)

Internally, coroutines are based on Python generators, but aren’t exactly the same thing.
Coroutines return a coroutine object similar to how generators return a generator object.
Once you have a coroutine, you obtain(получать) its results with the await expression.
When a coroutine calls await, execution of the this coroutine is suspended(приостановленный)
until the awaitable completes. !!!!
This suspension allows other work to be completed while the coroutine is suspended “awaiting” some result.
In general, this result will be some kind of I/O like a database request or in our case an HTTP request.

Now, to allow our method to work properly with the async programming paradigm, we’ve introduced a while loop that
reads chunks of the image at a time and suspends execution while waiting for the I/O to complete. This allows the
event loop to loop through downloading the different images as each one has new data available during the download.
"""

import asyncio
import logging
import os
from time import time

import aiohttp

from .tutorial_download import setup_download_dir, get_links

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def async_download_link(session, directory, link):
    """
    Async version of the download_link method we've been using in the other examples.
    :param session: aiohttp ClientSession
    :param directory: directory to save downloads
    :param link: the url of the link to download
    :return:
    """
    download_path = directory / os.path.basename(link)
    async with session.get(link) as response:
        with download_path.open('wb') as f:
            while True:
                # await pauses execution until the 1024 (or less) bytes are read from the stream
                chunk = await response.content.read(1024)
                if not chunk:
                    # We are done reading the file, break out of the while loop
                    break
                f.write(chunk)
    logger.info('Downloaded %s', link)


# Main is now a coroutine
async def main():
    client_id = "4591084c070d7d4"
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    # We use a session to take advantage of tcp keep-alive
    # Set a 3 second read and connect timeout. Default is 5 minutes
    async with aiohttp.ClientSession(conn_timeout=3, read_timeout=3) as session:
        tasks = [(async_download_link(session, download_dir, l)) for l in get_links(client_id)]
        # gather aggregates all the tasks and schedules them in the event loop
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    ts = time()
    # Create the asyncio event loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        # Shutdown the loop even if there is an exception
        loop.close()
    logger.info('Took %s seconds to complete', time() - ts)
