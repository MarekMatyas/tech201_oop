from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tounge = True # These need to be set to some value
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tounge_to_smell(self):
        print("Do I say it smells or tastes nice?")


sidney = Snake()
# sidney.seek_heat()