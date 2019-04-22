import abc


# An abstract class (cannot be instantiated)
# representing an object that can be drawn on the screen
# and with state that can be updated
class GameObject(abc.ABC):
    @abc.abstractmethod
    def render(self, screen):
        pass

    @abc.abstractmethod
    def update(self, *args):
        pass
