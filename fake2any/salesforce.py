# -*- coding:utf-8 -*-
from plugin import Plugin
from faker import Factory
from pyforce import pyforce
class Salesforce(Plugin):
    """
    """
    def load(self):
        svc = pyforce.Client()
        svc.login(self._config["username"], self._config["password"])
        records = []
        for i in range(0, int(self._config["args"].rows)):
            record = {}
            record["type"] = self._config["sobj_type"]
            for column in self._config["columns"]:
                record[column["name"]] = self.getFakeColumnValue(column)
            records.append(record)
            #print(records)
        result = svc.create(records)
        print(result)