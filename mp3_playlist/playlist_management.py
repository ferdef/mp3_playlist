from glob import glob
from pathlib import Path
import logging
logger = logging.getLogger(__name__)


def get_subfolders(path='.'):
    paths = glob(os.path.join(path, '*/'))
    logger.info("{}".format(', '.join(paths)))
    return paths


def get_files(path):
    files = glob(os.path.join(path, '*.mp3'))
    logger.info('Found {} files'.format(len(files)))
    for f in files:
        logger.debug('{}'.format(f))
    return files


def create_playlist(path, filename, files, source):
    logger.info("Creating playlist {} in {}".format(filename, path))
    if len(files) == 0:
        return
    with open(Path(path) / filename, 'w', encoding='utf-8') as playlist_file:
        for f in files:
            f_path = str(Path(f).relative_to(source))
            logger.info("{}".format(f_path))
            playlist_file.write("\\{}{}".format(f_path, "\n"))
