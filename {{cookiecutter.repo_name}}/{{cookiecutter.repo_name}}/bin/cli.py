# coding: utf-8

import logging
logger = logging.getLogger(__name__)

class App(object):
    def __init__(self):
        pass

    def main(self):
        print "{{cookiecutter.repo_name}} up and running"

def main():
    App().main()


