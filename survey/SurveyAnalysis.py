from Link.DropGroupLinkModule import DropGroupLink
from Link.MathLinkModule import MathLink
from Link import LoadLinks
import copy
import json


def extract_queue(str_queue):
    link_queue = []
    for link_def in str_queue:
        link_queue.append(LoadLinks._load(link_def))
    return link_queue

class Analysis:

    def __init__(self, survey, queue=[]):
        loaded = json.loads(survey)
        self.working = copy.deepcopy(loaded)
        self.queue = queue

    def digest(self):
        for item in self.queue:
            self.working = item._process(self.working)
        return self.working

    def dump(self):
        dump_body = []
        for item in self.queue:
            dump_body.append(item._dump())
        return dump_body

    def drop_question_groups(self, groups):
        self.queue.append(DropGroupLink(groups))
        return self
 
    def math(self, operations):
        self.queue.append(MathLink(operations))
        return self

