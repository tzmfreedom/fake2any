# -*- coding:utf-8 -*-
from plugin import Plugin
import csv
from faker import Factory

class Csv(Plugin):
    def load(self):
        if self._config["append"]:
            f = open(self._config["outputfile"], "a+")
        else:
            f = open(self._config["outputfile"], "w")

        writer = csv.writer(f, lineterminator="\n", quoting=csv.QUOTE_ALL)

        if not(self._config["append"]):
            writer.writerow([column["name"] for column in self._config["columns"]])
        for i in range(0, int(self._config["args"].rows)):
            writer.writerow([self.getFakeColumnValue(column) for column in self._config["columns"]])
        f.close()