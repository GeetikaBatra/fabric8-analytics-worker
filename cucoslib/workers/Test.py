import os
import json
from selinon import FatalTaskError
from cucoslib.base import BaseTask

class Test(BaseTask):
    _analysis_name = 'Test'
    schema_ref = None


    def execute(self, arguments):
        file = arguments.get("file")
        with open(file, 'r') as f:
            result = f.read()
        return {'result': result}
