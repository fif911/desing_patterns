"""
Lets see if we can speed this up using a ProcessPoolExecutor.

cpu-bound task multiprocessing ( creating the thumbnails in parallel)

The create_thumbnail method is identical to the last script. The main difference
is the creation of a ProcessPoolExecutor. The executor’s map method is used to create the thumbnails in parallel.\
By default, the ProcessPoolExecutor creates one subprocess per CPU.
Running this script on the same 160 images took 1.05 seconds—2.2 times faster!
Took 0.812260627746582 for 467 images
Took 0.9957497119903564 for 640 images
"""

import logging
from pathlib import Path
from time import time
from functools import partial

from concurrent.futures import ProcessPoolExecutor

from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def create_thumbnail(size, path):
    """
    Creates a thumbnail of an image with the same name as image but with
    _thumbnail appended before the extension. E.g.:

    A new thumbnail image is created with the name image_thumbnail.jpg

    :param size: A tuple of the width and height of the image
    :param path: The path to the image file
    :return: None
    """
    path = Path(path)
    name = path.stem + '_thumbnail' + path.suffix
    thumbnail_path = path.with_name(name)
    image = Image.open(path)
    image.thumbnail(size)
    image.save(thumbnail_path)


def main():
    ts = time()
    # Partially apply the create_thumbnail method, setting the size to 128x128
    # and returning a function of a single argument.
    thumbnail_128 = partial(create_thumbnail, (128, 128))
    i = sum(1 for _ in Path('images').iterdir())

    # Create the executor in a with block so shutdown is called when the block
    # is exited.
    with ProcessPoolExecutor() as executor:
        executor.map(thumbnail_128, Path('images').iterdir())
    logging.info('Took %s', time() - ts)

    logging.info('Took %s for %d images', time() - ts, i)


if __name__ == '__main__':
    main()
