from abc import ABCMeta, abstractmethod
class Link:
    __metaclass__ = ABCMeta

    @abstractmethod
    def _process(self, response): raise NotImplementedError
    
    @abstractmethod
    def _dump(self): raise NotImplementedError