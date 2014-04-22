import random 
class node:
    """A simple example node"""
    height = None
    name = None

    def __init__(self):
        self.height = random.randint(57, 272)
    def get_name(self):
        return self.name
