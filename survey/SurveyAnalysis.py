from Link.DropGroupLinkModule import DropGroupLink
from Link.MathLinkModule import MathLink
import copy
import json

class Analysis:

    def __init__(self, survey):
        loaded = json.loads(survey)
        self.working = copy.deepcopy(loaded)
        self.queue = []
 
    def digest(self):
        for item in self.queue:
            self.working = item._process(self.working)
        return self.working

    def drop_question_groups(self, groups):
        self.queue.append(DropGroupLink(groups))
        return self
 
    def math(self, operations):
        self.queue.append(MathLink(operations))
        return self

