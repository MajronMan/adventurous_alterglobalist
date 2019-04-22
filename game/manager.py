from game_objects.button import Button


class Manager:
    def __init__(self):
        self.objects = []

    def render(self, screen):
        for obj in self.objects:
            obj.render(screen)

    def add_object(self, obj):
        self.objects.append(obj)

    def get_buttons(self):
        # get those objects which are buttons
        return filter(lambda x: issubclass(type(x), Button), self.objects)
