import abc


class Observer(abc.ABC):
    @abc.abstractmethod
    def notify(self, notifier):
        pass
