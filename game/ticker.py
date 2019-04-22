class Ticker:
    def __init__(self, game):
        self.events = set()
        self.game = game

    def add_event(self, e):
        self.events.add(e)

    def remove_event(self, e):
        return self.events.remove(e)

    def tick(self):
        for e in self.events:
            e.tick(self.game)
