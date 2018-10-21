import sys
import os
import argparse
import test_based as tb
import gui_based as gb
from log import logger


def parse_args():
    parser = argparse.ArgumentParser(description='Create Playlists from subfolders.')
    parser.add_argument('-s', '--source', required=True, help='Path where music subfolders are')
    parser.add_argument('-d', '--destination', required=True, help='Path where playlist files are placed')
    parser.add_argument('-g', '--graphical', action='store_true', help='Use Graphical interface')

    return parser.parse_args()


def main():
    args = vars(parse_args())
    logger.info('Mp3 Playlist Creator')

    if args['graphical']:
        gb.process(args)
    else:
        tb.process(args)


if __name__ == '__main__':
    main()
