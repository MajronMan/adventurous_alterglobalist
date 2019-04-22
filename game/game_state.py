from abstract.notifier import Notifier


class GameState(Notifier):
    def __init__(self):
        self.score = 0
        self.observers = set()

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify(self)

    def update_score(self, delta):
        self.score += delta
        self.notify_observers()

    def can_afford(self, value):
        return self.score >= value
