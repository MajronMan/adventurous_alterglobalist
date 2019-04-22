from game.game import Game


# Punkt początkowy: wykonaj `python main.py` w terminalu
# aby uruchomić grę.
if __name__ == '__main__':
    # Stwórz obiekt gry
    game = Game()
    # Uruchom główną pętlę w której działa cały program
    game.loop()
