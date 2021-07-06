# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.

class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return f'I am a bear and I am making this sound: {self.sound}'
