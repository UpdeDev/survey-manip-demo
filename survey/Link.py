from abc import ABCMeta, abstractmethod
class Link:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self, response): raise NotImplementedError
    
class FilterLink(Link):
    def __init__(self, filters):
        self.filters = filters

    def process(self, filters):
        print("foo")

class MathLink(Link):
    def sum(self, target, response):
        return -1

    def __init__(self, target, operation):
        self.target = target
        self.operation = operation

    def process(self, response):
        operation_switch = {
            "sum": self.sum
        }
        opfunc = operation_switch.get(self.operation)
        if(opfunc == None):
            raise ValueError

        return opfunc(self.target, response)