# coding: utf-8

import argparse
import logging
logger = logging.getLogger(__name__)


class App(object):

    """ {{cookiecutter.repo_name}} main entry point class"""

    def __init__(self):
        self.args_parser = argparse.ArgumentParser()

    def _init_args(self):
        self.args_parser.add_argument('-d', '--debug',
                                      dest='debug',
                                      help='Enable debug mode',
                                      action='store_true'
                                      )

    def _configure_loggers(self, args):
        """ {{cookiecutter.repo_name}} loggers configuration"""
        if args.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    def main(self):
        """ {{cookiecutter.repo_name}} main entry point method"""
        self._init_args()
        args = self.args_parser.parse_args()
        self._configure_loggers(args)

        logger.info("{{cookiecutter.repo_name}} up and running")


def main():
    """ {{cookiecutter.repo_name}} main entry point method called in setup.py"""
    App().main()
