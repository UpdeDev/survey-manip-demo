from Link import FilterLink, MathLink
import copy

class Analysis:

    def __init__(self, survey):
        self.golden = copy.deepcopy(survey)
        self.working = copy.deepcopy(survey)
        self.queue = []

    def digest(self):
        for item in self.queue:
            self.working = item.process(self.working)
        return self.working

    def filter(self, filters):
        self.queue.append(FilterLink(filters))
        return self

    def math(self, targets, operations):
        self.queue.append(MathLink(targets, operations))
        return self

