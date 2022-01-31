"""
https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
"""

import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png','image/gif'}


def get_links(client_id):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = Request('https://api.imgur.com/3/gallery/random/random/', headers=headers, method='GET')
    with urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))

    links = [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]
    logger.info(f"links len = {len(links)}")
    return links


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
