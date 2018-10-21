import os
from playlist_management import get_subfolders, get_files, create_playlist
from log import logger


def process(args):
    logger.info('Text Based')
    folders = get_subfolders(path=args['source'])
    for folder in folders:
        files = get_files(path=folder)
        logger.info('Folder {}'.format(folder.strip(os.sep)))
        filename = "{}{}".format(os.path.basename(folder.strip(os.sep)), '.m3u')
        create_playlist(path=args['destination'], filename=filename, files=files, source=args['source'])
