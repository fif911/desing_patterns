"""LETS TEST a CPU-bound task

Now that we have all these images downloaded , we can use them to test a CPU-bound task.
We can create thumbnail versions of all the images in both a single-threaded, single-process
script and then test a multiprocessing-based solution.

Here is our initial script.

This script iterates over the paths in the images folder and for each path it runs the create_thumbnail function
Running this script on 160 images totaling 36 million takes 2.32 seconds.
Took 1.3055264949798584 for 288 images
Took 1.8584482669830322 for 544 images
"""
import logging
from pathlib import Path
from time import time

from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def create_thumbnail(size, path):
    """
    Creates a thumbnail of an image with the same name as image but with
    _thumbnail appended before the extension.  E.g.:

    >>> create_thumbnail((128, 128), 'image.jpg')

    A new thumbnail image is created with the name image_thumbnail.jpg

    :param size: A tuple of the width and height of the image
    :param path: The path to the image file
    :return: None
    """
    image = Image.open(path)
    image.thumbnail(size)
    path = Path(path)
    name = path.stem + '_thumbnail' + path.suffix
    thumbnail_path = path.with_name(name)
    image.save(thumbnail_path)


def main():
    ts = time()
    i = 0

    for image_path in Path('images').iterdir():
        create_thumbnail((128, 128), image_path)
        i += 1
    logging.info('Took %s for %d images', time() - ts, i)


if __name__ == '__main__':
    main()
