import pygame

from game_objects.game_object import GameObject


class Button(GameObject):
    font_color = (100, 0, 100)
    background_color = (20, 20, 20)
    # space around the text
    padding = 5

    def __init__(self, label, position, onClick):
        self.onClick = onClick
        self.font = pygame.font.SysFont("Arial", 30)
        self.update(label, position)

    def update(self, label=None, position=None):
        if label is not None:
            self.text = self.font.render(label, True, self.font_color)
        if position is not None:
            x0 = position[0]
            y0 = position[1]
        else:
            x0 = self.rect.x
            y0 = self.rect.y

        w, h = self.text.get_size()
        self.rect = pygame.Rect(
            x0, y0,
            w + 2 * self.padding, h)

    def render(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect)
        screen.blit(self.text, (self.rect.x + self.padding,
                                self.rect.y))

    def collides(self, coords):
        return self.rect.collidepoint(coords)
