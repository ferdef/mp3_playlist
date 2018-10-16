import sys
import logging
from glob import glob
logger = logging.getLogger(__name__)


def setup_logger():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def get_subfolders(path='.'):
    paths = glob('*/')
    for path in paths:
        logger.info("{}".format(path))


def main():
    setup_logger()
    logger.info('Mp3 Playlist Creator')
    get_subfolders()


if __name__ == '__main__':
    main()
