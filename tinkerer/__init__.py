import os

MAJOR = 3
MINOR = 1
PATCH = 0

APP_NAME = 'mc-tinkerer'
APP_AUTHOR = 'Dmitri McGuckin'
APP_EMAIL = 'dmitri@mandatoryfun.xyz'
APP_DESCRIPTION = 'An MC Modpack builder, an alternative to both the twitch\
                   client pack editor and editing manifest jsons manually.'
APP_URL = 'https://github.com/dmitri-mcguckin/tinkerer'
APP_LICENSE = 'MIT'
APP_VERSION = "{}.{}.{}".format(MAJOR, MINOR, PATCH)
APP_DIRECTORY = os.path.expanduser('~/.config/tinkerer')
MC_PACKS_DIR = APP_DIRECTORY + os.sep + 'mc-packs' + os.sep

DEBUG = False