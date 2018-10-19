import sys
import os
import logging
from glob import glob
import argparse
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logger():
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def parse_args():
    parser = argparse.ArgumentParser(description='Create Playlists from subfolders.')
    parser.add_argument('-s', '--source', required=True, help='Path where music subfolders are')
    parser.add_argument('-d', '--destination', required=True, help='Path where playlist files are placed')
    parser.add_argument('-g', '--graphical', action='store_true', help='Use Graphical interface')

    return parser.parse_args()


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


def create_playlist(path, filename, files):
    logger.info("Creating playlist {} in {}".format(filename, path))
    with open(Path(path) / filename, 'w', encoding='utf8') as playlist_file:
        for f in files:
            f_path = Path(f)
            logger.info("{} - {}".format(f, f_path))
            playlist_file.write("{}{}".format(f, "\n"))


def text_based(args):
    logger.info('Text Based')
    folders = get_subfolders(path=args['source'])
    for folder in folders:
        files = get_files(path=folder)
        logger.info('Folder {}'.format(folder.strip(os.sep)))
        filename = "{}{}".format(os.path.basename(folder.strip(os.sep)), '.m3u')
        create_playlist(path=args['destination'], filename=filename, files=files)


def gui_based(args):
    logger.info('GUI Based. Not yet implemented')


def main():
    args = vars(parse_args())
    setup_logger()
    logger.info('Mp3 Playlist Creator')

    if args['graphical']:
        gui_based(args)
    else:
        text_based(args)


if __name__ == '__main__':
    main()
