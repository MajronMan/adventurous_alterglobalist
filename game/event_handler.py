import pygame


class EventHandler:
    def __init__(self, game):
        self.game = game

    def handle(self):
        for event in pygame.event.get():
            # X was pressed
            if event.type == pygame.QUIT:
                self.handle_quit(event)
            # mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse(event)
            # key press
            elif event.type == pygame.KEYDOWN:
                self.handle_keyboard(event)

    def handle_quit(self, event):
        self.game.exit()

    def handle_mouse(self, event):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.game.manager.get_buttons():
            if button.collides(mouse_pos):
                button.onClick(self.game)
                break

    def handle_keyboard(self, event):
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            self.game.shutdown()
