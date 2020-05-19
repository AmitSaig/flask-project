import random
import string

class Instrument(dict):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def create_id(stringLength=8):
        numbers = string.digits
        return ''.join(random.choice(numbers) for i in range(stringLength))

class User(dict):
    def __init__(self, name, id, playing):
        self.name = name
        self.id = id
        self.playing = playing

    def create_id(stringLength=8):
        numbers = string.digits
        return ''.join(random.choice(numbers) for i in range(stringLength))