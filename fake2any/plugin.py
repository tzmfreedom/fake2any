# -*- coding:utf-8 -*-
from faker import Factory
from pyforce import pyforce
class Plugin:
    """
    """
    def __init__(self, config):
        self._fake = Factory.create(config["args"].language)
        self._config = config

    def load(self):
        pass

    def getFakeColumnValue(self, column):
        method = getattr(self._fake, column["type"])
        try:
            return method()
        except AttributeError:
            return ""
