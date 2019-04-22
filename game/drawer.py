import pygame


class Drawer:
    def __init__(self):
        # create a screen with size of the display
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # load an image to be used as the background
        self.background = pygame.image.load("./wafle.jpg")

    def draw(self, manager):
        # draw background
        self.screen.blit(self.background, (0, 0))
        # pass screen to manager to render game objects
        manager.render(self.screen)
        # pass changes to the display
        pygame.display.update()
