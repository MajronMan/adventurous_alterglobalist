import pygame

from game.drawer import Drawer
from game.event_handler import EventHandler
from game.game_state import GameState
from game.manager import Manager
from game.ticker import Ticker

from game_objects.text import Text
from game_objects.button import Button

from abstract.recurring_event import RecurringEvent


class Game:
    def __init__(self):
        # initialize imported components
        pygame.init()
        # number of frames rendered per second
        # (equal to number of loop turns)
        self.FPS = 60
        # clock to synchronize ticks with desired FPS
        self.clock = pygame.time.Clock()
        # main loop condition
        self.running = True

        # initialize subsystems
        self.drawer = Drawer()
        self.handler = EventHandler(self)
        self.game_state = GameState()
        self.manager = Manager()
        self.ticker = Ticker(self)

    def initialize(self):
        # create game objects from scaffold
        # and add them to proper subsystems
        scaffold = Scaffold()
        for obj in scaffold.objects:
            self.manager.add_object(obj)

        for obs in scaffold.observers:
            self.game_state.add_observer(obs)

        for e in scaffold.recurring_events:
            self.ticker.add_event(e)

    def shutdown(self):
        # this will break main loop
        self.running = False

    def exit(self):
        # close all imported components
        pygame.quit()
        # force exit program
        exit(1)

    def loop(self):
        self.initialize()

        # main loop
        while self.running:
            # synchronize
            self.clock.tick(self.FPS)
            # notify ticker
            self.ticker.tick()

            # render game objects
            self.drawer.draw(self.manager)
            # respond to events
            self.handler.handle()

        self.exit()


class Scaffold:
    def __init__(self):
        # create a text showing the score
        # which updates on each change of game state
        score = Text("0$", (300, 0),
                     lambda observer, notifier:
                     observer.update(
            "{}$".format(notifier.score)))

        self.objects = [
            score,
            Button("+1$", (100, 100),
                   lambda game: game.game_state.update_score(1)),
            Button("+5$", (100, 150),
                   lambda game: game.game_state.update_score(5))
        ]

        self.observers = [
            score
        ]

        # create an event adding 1$ each second
        self.recurring_events = [
            RecurringEvent(60, lambda game: game.game_state.update_score(1))
        ]
