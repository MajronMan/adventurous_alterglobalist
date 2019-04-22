class RecurringEvent:
    def __init__(self, period, onFire):
        self.ticks = 0
        self.period = period
        self.onFire = onFire

    def tick(self, game):
        self.ticks += 1
        if self.ticks >= self.period:
            self.ticks = 0
            self.onFire(game)
