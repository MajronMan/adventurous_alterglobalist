import pygame

from game_objects.game_object import GameObject
from abstract.observer import Observer


# A game object which consists only of a text
class Text(GameObject, Observer):
    font_color = (100, 0, 100)

    def __init__(self, label, position, onNotify=None):
        self.onNotify = onNotify
        self.font = pygame.font.SysFont("Arial", 30)
        self.update(label, position)

    def notify(self, notifier):
        if self.onNotify is not None:
            self.onNotify(self, notifier)

    def update(self, label=None, position=None):
        if label is not None:
            self.label = label
        if position is not None:
            self.position = position
        self.text = self.font.render(self.label, True, self.font_color)

    def render(self, screen):
        screen.blit(self.text, self.position)
